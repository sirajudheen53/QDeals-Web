from django.contrib.auth.models import User
from rest_framework import serializers
from .models import QUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model: User
        fields: ('first_name', 'last_name', 'email')

class QUserSerializer(serializers.ModelSerializer):
    user = UserSerializer
    class Meta:
        model:QUser
        fields: '__all__'
