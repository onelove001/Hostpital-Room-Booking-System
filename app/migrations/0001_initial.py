# Generated by Django 4.1.5 on 2023-01-17 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Coach",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("coach_firstname", models.CharField(default="", max_length=50)),
                ("coach_lastname", models.CharField(default="", max_length=50)),
                ("coach_address", models.CharField(max_length=50)),
                ("coach_mobile", models.CharField(max_length=12)),
                ("date_created", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Membership",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("membership_name", models.CharField(max_length=50)),
                ("maximum_coach", models.CharField(max_length=2)),
                ("membership_description", models.CharField(max_length=250)),
                ("membership_price", models.CharField(max_length=50)),
                ("date_created", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("mobile_number", models.CharField(max_length=12, null=True)),
                ("address_location", models.CharField(max_length=200, null=True)),
                ("date_created", models.DateTimeField(auto_now=True)),
                (
                    "user_profile",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Class",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("class_name", models.CharField(max_length=50)),
                ("class_description", models.CharField(max_length=50)),
                ("date_created", models.DateTimeField(auto_now=True)),
                (
                    "coach",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.coach"
                    ),
                ),
            ],
        ),
    ]
