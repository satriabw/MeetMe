from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point
from location_field.models.plain import PlainLocationField




# Create your models here.


class UserProfile(models.Model):
    """
    Description: Model Description
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    sex = models.CharField(max_length=50)
    photo = models.ImageField('photo', blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    location = PlainLocationField(based_fields=['location'], zoom=7, null=True)
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
    user = models.ForeignKey(UserProfile, null=True, related_name='interest')
    interest = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.interest