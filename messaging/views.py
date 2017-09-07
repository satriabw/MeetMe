from django.shortcuts import render
from rest_framework import generics
from messaging.models import Message, MessageRecipient
from messaging.serializers import MessageSerializer, MessageRecipientSerializer

# Create your views here.

# class CreateMessage(generics.CreateAPIView):
# 	model = Message
# 	serializers = MessageSerializer
	
