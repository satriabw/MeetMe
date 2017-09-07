from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from account.permissions import *
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.
# class InterestMatrixList(generics.ListCreateAPIView):
#     model = InterestMatrix
#     queryset =