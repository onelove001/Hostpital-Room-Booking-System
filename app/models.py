from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=12, null=True)
    address_location = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.user_profile.username


class Coach(models.Model):
    id = models.AutoField(primary_key=True)
    coach_firstname = models.CharField(max_length=50, default="")
    coach_lastname = models.CharField(max_length=50, default="")
    coach_address = models.CharField(max_length=50)
    coach_mobile = models.CharField(max_length=12)
    date_created = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.coach_firstname
        

class Class(models.Model):
    id = models.AutoField(primary_key=True)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=50)
    class_description = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.class_name


class Membership(models.Model):
    id = models.AutoField(primary_key = True)
    membership_name = models.CharField(max_length = 50)
    maximum_coach = models.CharField(max_length=2)
    membership_description = models.CharField(max_length = 250)
    membership_price = models.CharField(max_length = 50)
    date_created = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.membership_name

SCHEDULE = (
    ("everyday",  "everyday"),
    ("every4days",  "every4days"),
    ("every2days",  "every2days"),
)

class Gym(models.Model):
    id = models.AutoField(primary_key=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    membership_id = models.ForeignKey(Membership, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    schedule = models.CharField(max_length=20, choices=SCHEDULE)
    status = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.profile.user_profile.username

