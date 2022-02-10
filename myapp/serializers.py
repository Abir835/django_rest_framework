from abc import ABC

from rest_framework import serializers
from myapp.models import Contact


# class ContactSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     title = serializers.CharField(max_length=255)
#     email = serializers.CharField(max_length=255)
#
#     def create(self, validated_data):
#         return Contact.objects.create(**validated_data)


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'title', 'email']
