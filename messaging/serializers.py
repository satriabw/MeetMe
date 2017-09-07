from rest_framework import serializers
from django.contrib.auth.models import User
from messaging.models import Message, MessageRecipient

class MessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Message
		field = ('creator', 'created_at', 'message_body', 'parent_message')

class MessageRecipientSerializer(serializers.ModelSerializer):
	class Meta:
		model = MessageRecipient
		field = ('message', 'recipient', 'is_read')