from django.shortcuts import render
from django.contrib.auth.models import User,Group
from .models import *
from rest_framework import viewsets,generics
from rest.serializers import *

class EzoneViewSet(viewsets.ModelViewSet):
    queryset=Ezone.objects.all()
    serializer_class=EzoneSerializer
class ContactsViewSet(viewsets.ModelViewSet):
    queryset=Contacts.objects.all()
    serializer_class=ContactsSerializer
class BranchesViewSet(viewsets.ModelViewSet):
    queryset=Branches.objects.all()
    serializer_class=BranchesSerializer
