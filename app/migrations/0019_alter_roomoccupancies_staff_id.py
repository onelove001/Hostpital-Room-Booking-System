# Generated by Django 4.1.3 on 2023-10-18 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0018_alter_roomoccupancies_staff_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="roomoccupancies",
            name="staff_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.staff"
            ),
        ),
    ]