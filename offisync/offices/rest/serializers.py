from cities_light.models import City, Country
from rest_framework import serializers

from offices.models import Office


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["id", "name"]


class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = City
        fields = ["id", "name", "country"]


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = [
            "id",
            "name",
        ]

    def get_current_temperature(self, obj):
        temperature_data = self.context.get("temperature_data", {})
        return temperature_data.get(obj.id)


class OfficeTemperatureSerializer(serializers.ModelSerializer):
    current_temperature = serializers.SerializerMethodField()
    city = CitySerializer(read_only=True)

    class Meta:
        model = Office
        fields = [
            "id",
            "name",
            "city",
            "address",
            "current_temperature",
            "latitude",
            "longitude",
        ]

    def get_current_temperature(self, obj):
        temperature_data = self.context.get("temperature_data", {})
        return temperature_data.get(obj.id)
