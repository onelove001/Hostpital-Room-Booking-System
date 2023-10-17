from django.db import models
from django.contrib.auth.models import *


GENDER = ( ("M", "M"), ("F", "F"),)


class CustomUser(AbstractUser):
    accout_choices      = ( (1, 1), (2, 2), )
    account_type        = models.CharField(max_length = 9, choices = accout_choices, default = 2)
    

class Patient(models.Model):
    id = models.AutoField(primary_key=True)
    user_profile = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    gender = models.CharField(choices = GENDER, max_length=20)
    dateOfBirth = models.DateField()
    phone_no = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.user_profile.username


class Room(models.Model):
    id = models.AutoField(primary_key=True)
    room_number = models.IntegerField()
    beds = models.IntegerField()
    status = models.BooleanField()
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