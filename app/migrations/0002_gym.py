# Generated by Django 4.1.5 on 2023-01-17 22:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Gym",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "schedule",
                    models.CharField(
                        choices=[
                            ("everyday", "everyday"),
                            ("every4days", "every4days"),
                            ("every2days", "every2days"),
                        ],
                        max_length=20,
                    ),
                ),
                ("date_created", models.DateTimeField(auto_now=True)),
                (
                    "class_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.class"
                    ),
                ),
                (
                    "membership_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.membership"
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.profile"
                    ),
                ),
            ],
        ),
    ]