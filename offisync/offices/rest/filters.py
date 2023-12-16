import django_filters
from offices.models import Office


class OfficeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Office
        fields = ['name']
