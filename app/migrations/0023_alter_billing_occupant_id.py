# Generated by Django 4.1.3 on 2023-10-18 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0022_remove_billing_patient_id_billing_occupant_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="billing",
            name="occupant_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.roomoccupancies"
            ),
        ),
    ]