import datetime
import requests
import json
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import login, authenticate
from .serializers import RegisterSerializer, UserProfileSerializer
from .models import UserProfile
from django.contrib.auth.models import User

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
#BASE_URL = 'https://meetme-gemastik.herokuapp.com/api/v1/account/user-interest/'
BASE_URL = 'http://127.0.0.1:8000/api/v1/account/user-interest/'


class AuthRegister(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, format=None):
        account = self.serializer_class(data=request.data)
        if account.is_valid():
            user = account.save()
            user_profile = UserProfile(user=user)
            user_profile.created_at = datetime.datetime.now()
            user_profile.save()
            user_prof = UserProfile.objects.get(user=user)

            data = {
                "user": account.data,
                'user_profile_id' : user_prof.id,
                'device_token': user_prof.device_token,
                "token": jwt_encode_handler(jwt_payload_handler(user))
            }
            return Response(data)
        return Response(account.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthLogin(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        data = request.data
        email = data.get('email', None)
        password = data.get('password', None)

        username = self.get_username_by_email(email, password)
        if username is None:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)

        account = authenticate(username=username, password=password)
        # Generate token and add it to the response object
        if account is not None:
            login(request, account)
            user_profile = UserProfile.objects.get(user=account)
            user_profile_ser = UserProfileSerializer(instance=user_profile)
            return Response({
                "user" : user_profile_ser.data,
                "token": jwt_encode_handler(jwt_payload_handler(account))
            }, status=status.HTTP_200_OK)

        return Response({
            'status': 'Unauthorized',
            'message': 'Username/password combination invalid.'
        }, status=status.HTTP_401_UNAUTHORIZED)

    def get_username_by_email(self, email, password):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                username = user.get_username()
            return username
        except User.DoesNotExist:
            return None


class PostToUserInterest(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, Format=None):
        data = request.data
        user_id = data.get("user", None)
        interests = data.get('interest', None).split(",")
        token = data.get('token', None)
        response = {}
        # change the url later
        url = BASE_URL
        for interest in interests:
            values = {
                'user' : user_id,
                'interest' : interest
            }
            headers = {"content-type": "application/json", 'Authorization' : 'jwt '+token}
            req = requests.post(url, data=json.dumps(values), headers=headers)
            key = 'interest_'+interest
            response[key] = req.text

        return Response({
            'user' : user_id,
            'interest' : data.get('interest')
        },status=status.HTTP_200_OK)