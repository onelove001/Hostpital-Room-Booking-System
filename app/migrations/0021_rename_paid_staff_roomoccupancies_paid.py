# Generated by Django 4.1.3 on 2023-10-18 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0020_rename_paid_roomoccupancies_paid_staff"),
    ]

    operations = [
        migrations.RenameField(
            model_name="roomoccupancies",
            old_name="paid_staff",
            new_name="paid",
        ),
    ]