from django.contrib import admin
from .models import *

class UserProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile, UserProfileAdmin)


class UserInterestAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserInterest, UserInterestAdmin)


class InterestAdmin(admin.ModelAdmin):
    pass


admin.site.register(Interest, InterestAdmin)

