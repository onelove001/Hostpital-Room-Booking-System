# Generated by Django 4.1.3 on 2023-10-18 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0013_remove_roomoccupancies_paid_staff_patient_staff_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="medication",
            name="staff",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="app.staff"
            ),
        ),
    ]