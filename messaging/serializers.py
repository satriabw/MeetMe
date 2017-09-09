from rest_framework import serializers
# from django.contrib.auth.models import User
from messaging.models import Message
from fcm_django.models import FCMDevice

class MessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Message
		fields = ('creator', 'recipient', 'created_at', 'message_body')

class FCModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = FCMDevice
		fields = ('registration_id', 'name', 'active', 'user', 'device_id', 'type')