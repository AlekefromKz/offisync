from rest_framework import serializers
from employees.models import Employee, WorkHistory
from offices.rest.serializers import OfficeSerializer


class WorkHistorySerializer(serializers.ModelSerializer):
    office = OfficeSerializer(read_only=True)

    class Meta:
        model = WorkHistory
        fields = ['start_date', 'end_date', 'office']


class ActiveWorkHistorySerializer(WorkHistorySerializer):
    class Meta(WorkHistorySerializer.Meta):
        fields = WorkHistorySerializer.Meta.fields + ['last_checked']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employee_id', 'first_name', 'last_name']


class EmployeeWorkHistorySerializer(EmployeeSerializer):
    active_office = serializers.SerializerMethodField()
    previous_offices = WorkHistorySerializer(many=True, read_only=True)

    class Meta(EmployeeSerializer.Meta):
        model = Employee
        fields = [*EmployeeSerializer.Meta.fields, 'active_office', 'previous_offices']

    def get_active_office(self, obj):
        active_office = getattr(obj, 'active_office', [])
        return ActiveWorkHistorySerializer(active_office[0]).data if active_office else None
