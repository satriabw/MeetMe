from rest_framework import serializers
from .models import MessageModel


class MessageSerialzer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields = ('id', 'sender', 'body', 'recipient')