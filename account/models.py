from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    Description: Model Description
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    sex = models.CharField(max_length=50, null=True)
    device_token  = models.CharField(max_length=250, null=True, default="")
    occupation = models.CharField(max_length=250, null=True, blank=True)
    photo = models.ImageField('photo', blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    location_lat = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    location_lon = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    birth_place = models.CharField(max_length=50, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    class Meta:
        ordering = ['created_at']

class Interest(models.Model):
    """
    Description: Model Description
    """
    interest = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.interest


class UserInterest(models.Model):
    """
    Description: Model Description
    """
    user = models.ForeignKey(UserProfile, null=True, related_name='user_interest')
    interest = models.ForeignKey(Interest, null=True, related_name='user_interest')

    def __str__(self):
        return self.user.user.first_name + " " + self.user.user.last_name + ":" + self.interest.interest