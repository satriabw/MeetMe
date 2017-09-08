from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from account.permissions import *
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.
class InterestMatrixList(generics.ListCreateAPIView):
    model = InterestMatrix
    queryset = InterestMatrix.objects.all()
    serializer_class = GETInterestMatrixSerializer
    permission_classes = (AllowAny,)
