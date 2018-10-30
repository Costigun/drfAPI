from django.contrib.auth.models import User, Group
from rest.models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name','imgpath')

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ('type', 'value',)


class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = ('address', 'latitude', 'longitude',)


class CourseSerializer(serializers.ModelSerializer):
    contacts = ContactsSerializer(
        many=True
    )
    branches = BranchesSerializer(
        many=True
    )
    category = (

    )

    class Meta:
        model = Course
        fields = ('name', 'logo', 'category', 'description', 'contacts', 'branches',)

    def create(self, validated_data):
        contacts_data = validated_data.pop('contacts')
        branches_data = validated_data.pop('branches')
        course = Course.objects.create(**validated_data)
        for contacts_data in contacts_data:
            Contacts.objects.create(course=course, **contacts_data)
        for branches_data in branches_data:
            Branches.objects.create(course=course, **branches_data)
        return course


