from customers.models import Customer, Contact
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta: 
        model= Customer
        fields= "__all__"

class ContactSerializer(serializers.ModelSerializer):
    class Meta: 
        model= Contact
        fields= "__all__"