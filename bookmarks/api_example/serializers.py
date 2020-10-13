from django.contrib.auth.models import User, Group
from rest_framework import serializers
from images.models import Image


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['user', 'title', 'slug', 'url', 'image', 'description', 'created', 'users_like']