from django.db import models
from account.models import UserProfile


# Create your models here.
class MessageModel(models.Model):
    sender = models.ForeignKey(UserProfile, null=True, related_name="message_sender")
    body = models.TextField(blank=True, default="")
    recipient = models.ForeignKey(UserProfile, null=True, related_name="message_recipient")

    def __str__(self):
        return self.sender.user.username + ":"+ self.recipient.user.username + ":" + self.body