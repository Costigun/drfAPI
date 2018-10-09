from django.contrib.auth.models import User,Group
from rest.models import *
from rest_framework import serializers

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ('type','value')

class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = ('address','latitude','longitude')

class EzoneSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer(
        many=True
    )
    branches = BranchesSerializer(
        many=True
    )
    class Meta: 
        model = Ezone
        fields = ('id','name','logo','category','description','contacts','branches')

