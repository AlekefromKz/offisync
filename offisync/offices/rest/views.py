from rest_framework import mixins
import requests
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from employees.models import Employee
from employees.rest.serializers import EmployeeSerializer
from offices.models import Office
from .serializers import OfficeSerializer
from .filters import OfficeFilter


class OfficeViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    filterset_class = OfficeFilter

    def get_queryset(self):
        return Office.objects.select_related('city', 'city__country').all()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        queryset = self.filter_queryset(self.get_queryset())
        context['temperature_data'] = self.fetch_temperature_data_for_offices(queryset)
        return context

    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        office = self.get_object()
        active_employees = Employee.objects.filter(
            workhistory__office=office,
            workhistory__end_date__isnull=True
        ).distinct()

        page = self.paginate_queryset(active_employees)
        if page is not None:
            serializer = EmployeeSerializer(page, many=True, context={'request': request})
            return self.get_paginated_response(serializer.data)

        serializer = EmployeeSerializer(active_employees, many=True, context={'request': request})
        return Response(serializer.data)

    def fetch_temperature_data_for_offices(self, queryset):
        temperature_data = {}
        for office in queryset:
            if office.latitude and office.longitude:
                weather_data = self.get_current_temperature(office.latitude, office.longitude)
                if weather_data:
                    temperature_data[office.id] = weather_data.get('temperature')
        return temperature_data

    @staticmethod
    def get_current_temperature(latitude, longitude):
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
        try:
            response = requests.get(weather_url)
            response.raise_for_status()
            weather_data = response.json().get('current_weather')
            return {'temperature': weather_data.get('temperature')} if weather_data else None
        except requests.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None
