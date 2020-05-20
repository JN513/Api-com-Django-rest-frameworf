from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuario
from .serialize import UsuarioSerialize

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerialize

# Create your views here.
