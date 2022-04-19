from dataclasses import field
from rest_framework import serializers
from .models import *



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class loanserializer(serializers.ModelSerializer):
    class Meta:
        model = Liberty_Loan_database
        fields = "__all__"

class bvn_checkserializer(serializers.Serializer):
    bvn = serializers.CharField()