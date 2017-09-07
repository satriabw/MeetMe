from rest_framework import serializers
from account.models import Interest
from .models import *

class InterestMatrixSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestMatrix
        fields = ('id', 'interest', 'interest_pair', 'weight')
