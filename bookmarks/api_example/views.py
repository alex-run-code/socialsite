from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, GroupSerializer, ImageSerializer
from images.models import Image
from images.forms import ImageCreateForm
from rest_framework import generics
import django_filters.rest_framework
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages


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
    API endpoint showing all images
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Image.objects.all()
        try:
            slug = self.kwargs['slug']
            if slug is not None:
                queryset = queryset.filter(slug=slug)
        except KeyError:
            pass
        return queryset

    def post(self, request):
        if request.method == 'POST':
            form = ImageCreateForm(data=request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                new_item = form.save(commit=False)
                # assign current user to the item
                new_item.user = request.user
                new_item.save()
                messages.success(request, 'Image added successfully')
                # redirect to new created item detail
                return redirect(new_item.get_absolute_url())


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allow images to be viewed or edited
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticated]

