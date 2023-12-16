from django.contrib import admin
from .models import Employee, WorkHistory


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'first_name', 'last_name')
    search_fields = ('employee_id', 'first_name', 'last_name')

    def get_readonly_fields(self, request, obj=None):
        if obj:  # If editing an existing object, make employee_id readonly
            return ('employee_id',)
        return ()  # Otherwise, make it editable


@admin.register(WorkHistory)
class WorkHistoryAdmin(admin.ModelAdmin):
    autocomplete_fields = ['employee', 'office']
    list_display = ('employee', 'office', 'start_date', 'end_date')
    search_fields = ('employee__first_name', 'employee__last_name', 'office__name')
    list_filter = ('office', 'start_date', 'end_date')
