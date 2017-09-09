from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import *
import requests
from django.contrib.auth import authenticate
import json
BASE_URL = 'https://meetme-gemastik.herokuapp.com/api/v1/account/user/%s'
# BASE_URL = 'http://127.0.0.1:8000/api/v1/account/user/%s'


class MatchmakingEngine(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        data = request.data
        user_id = data.get('user')
        lat = data.get('location_lat')
        lon = data.get('location_lon')
        token = data.get('token')
        interests = data.get('interest').split(",")
        user_profile = UserProfile.objects.get(pk=user_id)
        self.update_location(lat, lon, user_profile, token)
        respon = []
        for interest in interests:
            users = []
            interest_obj = Interest.objects.get(pk=interest)
            interest_pair = InterestMatrix.objects.filter(interest_pair=interest_obj)
            pair = {'id': interest_obj.id, 'interest': interest_obj.interest,}
            for i in interest_pair:
                user_interest = UserInterest.objects.filter(interest=i.interest.id)
                for j in user_interest:
                    if int(j.user.id) != int(user_id):
                        interest = Interest.objects.get(pk=j.interest.id)
                        interest_ser = MatchmakingInterestSerializer(interest)
                        weight = i.weight
                        users.append({'id': j.user.id, 'interest': interest_ser.data, 'pair': pair, 'weight': weight})
            for u in users:
                user = UserProfile.objects.get(pk=u['id'])
                ser = MatchmakingEngineSerializer(user)
                res = {'user' : ser.data, 'interest' : u['interest'], 'pair': u['pair'], 'weight' : u['weight']}
                respon.append(res)
        return Response({'user': user_profile.id, 'location_lat': user_profile.location_lat,
                         'location_lon': user_profile.location_lon, 'data' : respon})

    def update_location(self, lat, lon,user,token):
        user_obj = User.objects.get(pk=user.user.id)
        user_obj = authenticate(username=user_obj.username, password=user_obj.password)
        user_prof = UserProfile.objects.get(user=user_obj)
        url = BASE_URL % user_prof.id
        values = {
            'location_lat' : float(lat),
            'location_lon' : float(lon),

        }
        url = url.rstrip()
        headers = {"content-type": "application/json", 'Authorization': 'jwt ' + token}
        res = requests.put(url, data=json.dumps(values), headers=headers)
        print(res.text)