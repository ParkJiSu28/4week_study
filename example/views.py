from rest_framework import generics,mixins
from .models import Exmodel
from .serializers import ExmodelSerializer
from django.shortcuts import get_object_or_404

# Create your views here.

class ExmodelListAPIView(generics.ListCreateAPIView):
    queryset = Exmodel.objects.all()
    serializer_class = ExmodelSerializer

class ExmodelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Exmodel.objects.all()
    serializer_class = ExmodelSerializer