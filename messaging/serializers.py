from rest_framework import serializers
# from django.contrib.auth.models import User
from messaging.models import Message

class MessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Message
		field = ('creator', 'created_at', 'message_body')