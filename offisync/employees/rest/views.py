from django.db.models import Prefetch
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins

from rest_framework.viewsets import GenericViewSet

from employees.models import Employee, WorkHistory
from employees.rest.filters import EmployeeFilter
from employees.rest.serializers import EmployeeWorkHistorySerializer


class EmployeeViewSet(
    mixins.ListModelMixin,
    GenericViewSet
):
    permission_classes = []
    queryset = Employee.objects.all().prefetch_related('workhistory_set__office')
    serializer_class = EmployeeWorkHistorySerializer
    filterset_class = EmployeeFilter

    def get_queryset(self):
        active_histories = WorkHistory.objects.filter(end_date__isnull=True).select_related('office')
        previous_histories = WorkHistory.objects.filter(end_date__isnull=False).select_related('office')

        return Employee.objects.prefetch_related(
            Prefetch('workhistory_set', queryset=active_histories, to_attr='active_work_histories'),
            Prefetch('workhistory_set', queryset=previous_histories, to_attr='previous_work_histories')
        )
