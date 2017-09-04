
import datetime
import requests
import json
from urllib.request import Request, urlopen  # Python 3
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import login, authenticate
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer
from .models import UserProfile
from django.contrib.auth.models import User

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

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
            data = {
                "user": account.data,
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
            user_ser = UserSerializer(instance=account)
            return Response({
                "user": user_ser.data,
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
        url = 'http://127.0.0.1:8000/api/v1/account/user-interest/'
        try:
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
                'data' : response
            },status=status.HTTP_200_OK)
        except Exception:
            return Response({
                'data' : "error"
            },status=status.HTTP_400_BAD_REQUEST)


# class AuthLogin(APIView):
#     permission_classes = (AllowAny,)
#
#     def post(self, request, format=None):
#         ser = LoginSerializer(data=request.data)
#         if ser.is_valid():
#             try:
#                 user = User.objects.get(email=ser.validated_data)
#                 up = UserProfile.objects.get(user_email=ser.validated_data)
#                 up.device_token = request.data['device_token']
#                 up.save()
#             except User.DoesNotExist:
#                 return Response({"detail": 'User not found.'}, status=status.HTTP_400_BAD_REQUEST)
#             user_ser = UserSerializer(instance=user)
#             data = {
#                 "user": user_ser.data,
#                 "token": jwt_encode_handler(jwt_payload_handler(user))
#             }
#             return Response(data)
#         return Response(ser.errors, status=status.HTTP_401_UNAUTHORIZED)