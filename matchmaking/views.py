from rest_framework.permissions import IsAuthenticated, AllowAny
from account.permissions import *
from rest_framework import generics
from .serializers import *


class InterestMatrixList(generics.ListCreateAPIView):
    model = InterestMatrix
    queryset = InterestMatrix.objects.all()
    serializer_class = GETInterestMatrixSerializer
    permission_classes = (UserPermissionsAll,)
