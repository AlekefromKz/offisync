from django.db import models


class Employee(models.Model):
    employee_id = models.CharField(max_length=20, primary_key=True, unique=True)
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"


class WorkHistory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    office = models.ForeignKey("offices.Office", on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    last_checked = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.employee} - {self.office}"

    class Meta:
        verbose_name = "Work history"
        verbose_name_plural = "Work histories"
        constraints = [
            models.UniqueConstraint(
                fields=["employee"],
                condition=models.Q(end_date__isnull=True),
                name="unique_active_work_history",
            )
        ]
