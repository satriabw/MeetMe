from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FileUploadParser, JSONParser
from rest_framework.response import Response
from .permissions import *
from rest_framework import generics
from account.models import UserProfile, Interest, UserInterest
from account.serializers import UserProfileSerializer, InterestSerializer, UserInterestSerializer
# Create your views here.

class UserProfileList(generics.ListAPIView):
    model = UserProfile
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated, UserPermissionsAll,)

    def lists(self):
        queryset = self.get_queryset()
        serializer = UserProfileSerializer(queryset, many=True)
        return Response(serializer.data)


class UserInterests(generics.ListCreateAPIView):
    model = UserInterest
    queryset = UserInterest.objects.all()
    serializer_class = UserInterestSerializer
    permission_classes = (IsAuthenticated,)

class UserInterestDetails(generics.RetrieveDestroyAPIView):
    model = UserInterest
    queryset = UserInterest.objects.all()
    serializer_class = UserInterestSerializer
    permission_classes = (IsAuthenticated, UserInterestDetailPermission,)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UserInterestSerializer(instance)
        return Response(serializer.data)


class UserProfileDetails(generics.RetrieveUpdateAPIView):
    model = UserProfile
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated, UserProfilePermission,)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UserProfileSerializer(instance)
        return Response(serializer.data)

class Interests(generics.ListCreateAPIView):
    model = Interest
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    permission_classes = (IsAuthenticated,)

class InterestDetails(generics.RetrieveDestroyAPIView):
    model = Interest
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
    permission_classes = (IsAuthenticated, UserPermissionsAll,)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = InterestSerializer(instance)
        return Response(serializer.data)

