from django.db.models import Prefetch
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from employees.models import Employee, WorkHistory
from employees.rest.filters import EmployeeFilter
from employees.rest.serializers import EmployeeWorkHistorySerializer


class EmployeeViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Employee.objects.all().prefetch_related("workhistory_set__office")
    serializer_class = EmployeeWorkHistorySerializer
    filterset_class = EmployeeFilter

    def get_queryset(self):
        active_office_queryset = WorkHistory.objects.filter(
            end_date__isnull=True
        ).select_related("office", "office__city", "office__city__country")
        previous_offices_queryset = WorkHistory.objects.filter(
            end_date__isnull=False
        ).select_related("office", "office__city", "office__city__country")

        return self.queryset.prefetch_related(
            Prefetch(
                "workhistory_set",
                queryset=active_office_queryset,
                to_attr="active_office",
            ),
            Prefetch(
                "workhistory_set",
                queryset=previous_offices_queryset,
                to_attr="previous_offices",
            ),
        )
