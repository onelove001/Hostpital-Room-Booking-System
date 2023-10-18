from django.db import models
from django.contrib.auth.models import *


GENDER = ( ("M", "M"), ("F", "F"),)


class CustomUser(AbstractUser):
    accout_choices      = ( (1, 1), (2, 2), )
    account_type        = models.CharField(max_length = 9, choices = accout_choices, default = 2)


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    room_number = models.IntegerField()
    beds = models.IntegerField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"Room {self.room_number}"


class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    user_profile = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.user_profile.username}"


class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    gender = models.CharField(choices = GENDER, max_length=20, default="")
    dob = models.DateField(null=True)
    phone_no = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.username


class Medication(models.Model):
    id = models.AutoField(primary_key=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    drug_prescription = models.TextField()
    created = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.patient_id.username}"


class RoomOccupancies(models.Model):
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    book_number = models.IntegerField(unique=True)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    date_in = models.DateField()
    date_out = models.DateField()
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.patient_id.username} - {self.room_id.room_number}"


class Billing(models.Model):
    id = models.AutoField(primary_key=True)
    occupant_id = models.ForeignKey(RoomOccupancies, on_delete=models.CASCADE)
    amount = models.IntegerField()
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_id} - {self.amount}"