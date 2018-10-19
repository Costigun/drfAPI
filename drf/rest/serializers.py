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
    
    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts')
        branches_data = validated_data.pop('branches')
        ezone = Ezone.objects.create(**validated_data)
        for contacts_data in contacts_data:
            Contacts.objects.create(ezone=ezone, **contacts_data)
        for branches_data in branches_data:
            Branches.objects.create(ezone=ezone, **branches_data)
        return ezone

