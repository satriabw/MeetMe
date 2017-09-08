from rest_framework import serializers
from account.models import Interest
from account.serializers import *
from .models import *


# class InterestMatrixSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = InterestMatrix
#         fields = ('id', 'interest', 'interest_pair', 'weight')
class InterestMatrixSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestMatrix
        fields = ('weight',)


class GETInterestMatrixSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestMatrix
        fields = ('id', 'interest', 'interest_pair','weight',)


class MatchmakingInterestSerializer(serializers.ModelSerializer):
    # interest_matrix = InterestMatrixSerializer(many=True, read_only=True)
    class Meta:
        model = Interest
        fields = ('id', 'interest', )


# class UserInterestMatchmakingSerializer(serializers.ModelSerializer):
#     user_interest = MatchmakingInterestSerializer(source="interest")
#     class Meta:
#         model = UserInterest
#         fields = ('id','user_interest')
#         fields = ('id','user_interest')

class MatchmakingEngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'occupation',  'location_lat', 'location_lon', )
