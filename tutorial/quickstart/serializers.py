from django.contrib.auth.models import *
from rest_framework import serializers
from tutorial.quickstart.models import *

#creating this API so that we can store the data as json


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User  #User table
        fields = ('url', 'username', 'email', 'groups')   #limit rows in the API (in json)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group   #Group table
        fields = ('url', 'name')

class HockeyTeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HockeyTeam   #Hockey table
        fields = ('teamname', 'city', 'coach', 'logo', 'mascot')