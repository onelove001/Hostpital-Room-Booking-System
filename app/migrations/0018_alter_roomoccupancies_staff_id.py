# Generated by Django 4.1.3 on 2023-10-18 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0017_alter_roomoccupancies_staff_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="roomoccupancies",
            name="staff_id",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="app.staff"
            ),
        ),
    ]
