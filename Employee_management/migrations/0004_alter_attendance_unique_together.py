# Generated by Django 5.1.1 on 2024-10-01 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee_management', '0003_alter_attendance_date'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together={('employee_id', 'status')},
        ),
    ]