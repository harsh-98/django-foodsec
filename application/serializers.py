from django.contrib.auth.models import  Group
from application.models import User, ColdStorage
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = User
            fields = ('username', 'email', 'password', 'role')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Group
            fields = ('url', 'name')

class ColdStorageSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = ColdStorage
            fields = ('owner', 'name', 'longitude', 'latitude', 'yieldType', 'space','empty')