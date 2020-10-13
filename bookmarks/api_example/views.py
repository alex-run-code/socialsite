from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer, ImageSerializer
from images.models import Image
from rest_framework import generics

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint allowing users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ImageList(generics.ListCreateAPIView):
    """
    API endpoint that allow images to be viewed or edited
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
   # permission_classes = [permissions.IsAuthenticated]


