from django.urls import include, path
from rest_framework.routers import DefaultRouter

from employees.rest.views import EmployeeViewSet
from offices.rest.views import OfficeViewSet

router = DefaultRouter()
router.register(r"employees", EmployeeViewSet, basename="employees")
router.register(r"offices", OfficeViewSet, basename="offices")

urlpatterns = [
    path("", include(router.urls)),
]
