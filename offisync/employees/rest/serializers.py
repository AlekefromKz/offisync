from rest_framework import serializers
from employees.models import Employee, WorkHistory
from offices.rest.serializers import OfficeSerializer


class WorkHistorySerializer(serializers.ModelSerializer):
    office = OfficeSerializer(read_only=True)

    class Meta:
        model = WorkHistory
        fields = ['office', 'start_date', 'end_date']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['employee_id', 'first_name', 'last_name']


class EmployeeWorkHistorySerializer(EmployeeSerializer):
    active_offices = WorkHistorySerializer(many=True, read_only=True, source='active_work_histories')
    previous_offices = WorkHistorySerializer(many=True, read_only=True, source='previous_work_histories')

    class Meta(EmployeeSerializer.Meta):
        model = Employee
        fields = [*EmployeeSerializer.Meta.fields, 'active_offices', 'previous_offices']
