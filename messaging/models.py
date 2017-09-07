from django.db import models
# from django.contrib.auth.models import User
from account.models import UserProfile

# Create your models here.
class Message(models.Model):
	creator = models.ForeignKey(UserProfile)
	created_at = models.DateTimeField(auto_now_add=True)
	message_body = models.TextField()
	parent_message = models.ForeignKey("self")

class MessageRecipient(models.Model):
	message = models.ForeignKey(Message)
	recipient = model.ForeignKey(UserProfile)
	is_read = models.BooleanField(default=False)