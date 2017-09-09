from django.db import models
# from django.contrib.auth.models import User
from account.models import UserProfile

# Create your models here.
class Message(models.Model):
	creator = models.ForeignKey(UserProfile, related_name='message_creator')
	recipient = models.ForeignKey(UserProfile, related_name='message_recipient')
	created_at = models.DateTimeField(auto_now_add=True)
	message_body = models.TextField()