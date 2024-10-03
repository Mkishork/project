from django.db import models
from django.utils import timezone


class Adding(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    # department = models.CharField(max_lenght=20)
    destination = models.CharField(max_length=80)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name} - {self.destination}"


class Attendance(models.Model):
    employee_id = models.ForeignKey(Adding, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.employee_id} - {self.date} - {self.status}"

    #  check if the 
    class Meta:
        unique_together = ('employee_id', 'date')
