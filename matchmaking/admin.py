from django.contrib import admin
from .models import InterestMatrix

# Register your models here.
class InterestMatrixAdmin(admin.ModelAdmin):
    pass


admin.site.register(InterestMatrix, InterestMatrixAdmin)