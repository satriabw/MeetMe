from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .serializers import *

class MatchmakingEngine(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        data = request.data
        user = data.get('user')
        interest = data.get('interest')

        interest = Interest.objects.get(pk=interest)
        interest_pair = InterestMatrix.objects.filter(interest_pair=interest)

        user = []
        respon = []


        for i in interest_pair:
            user_interest = UserInterest.objects.filter(interest=i.interest)
            for j in user_interest:
                interest = Interest.objects.get(pk=j.interest.id)
                interest_ser = MatchmakingInterestSerializer(interest)
                weight = i.weight
                user.append({'id': j.user.id, 'interest': interest_ser.data, 'weight': weight})

        unique = []
        for u in user:
            if u['id'] in unique:
                continue
            else:
                user = UserProfile.objects.get(pk=u['id'])
                ser = MatchmakingEngineSerializer(user)
                res = {'user' : ser.data, 'interest' : u['interest'], 'weight' : u['weight']}
                unique.append(u['id'])
                respon.append(res)

        # for w in weights:
        #     respon.append(w)

        return Response({'data' : respon})


    def update_location(self, lat, lon):
        pass
