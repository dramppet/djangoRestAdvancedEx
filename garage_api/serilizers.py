from rest_framework import serializers

from garage_api.models import Manufacture, Car


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacture
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'