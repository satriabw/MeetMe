from django.shortcuts import render
from rest_framework import generics
from messaging.models import Message
from fcm_django.models import FCMDevice
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from messaging.serializers import MessageSerializer

# Create your views here.

# class CreateMessage(generics.CreateAPIView):
# 	model = Message
# 	serializers = MessageSerializer

class MessagePosting(generics.ListCreateAPIView):
	model = Message
	queryset = Message.objects.all()
	serializer_class = MessageSerializer
	permission_class = (IsAuthenticated,)

class FCMPost(generics.ListCreateAPIView):
	model = FCMDevice
	device = FCMDevice.objects.all().first()
	permission_class = (IsAuthenticated.)
	#device.send_message(data={'test': 'test'})