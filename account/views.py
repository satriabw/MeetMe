from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.parsers import FileUploadParser, JSONParser
from rest_framework.response import Response
from rest_framework import generics
from account.models import UserProfile, Interest
from account.serializers import UserProfileSerializer, InterestSerializer
# Create your views here.

class UserProfileList(generics.ListAPIView):
    model = UserProfile
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def lists(self):
        queryset = self.get_queryset()
        serializer = UserProfileSerializer(queryset, many=True)
        return Response(serializer.data)


class UserProfileDetails(generics.RetrieveDestroyAPIView):
    model = UserProfile
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UserProfileSerializer(instance)
        return Response(serializer.data)

class Interests(generics.ListCreateAPIView):
    model = Interest
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer

class InterestDetails(generics.RetrieveDestroyAPIView):
    model = Interest
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = InterestSerializer(instance)
        return Response(serializer.data)