from rest_framework import serializers
from address.models import Addresses


class AddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = ['name', 'number', 'address']