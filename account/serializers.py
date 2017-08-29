from rest_framework import serializers
from django.contrib.auth.models import User
from account.models import UserProfile, Interest
from rest_framework import permissions


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ('id', 'user', 'interest')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'firstname', 'lastname', 'sex',  'email',
                  'photo', 'phone_number', 'location',
                  'birth_place', 'birth_date', 'created_at', 'updated_at')
        read_only_fields = ('id',)