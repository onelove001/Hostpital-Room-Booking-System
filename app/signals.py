from django.dispatch import receiver
from django.db.models.signals import *
from .models import *
import datetime

@receiver(post_save, sender = CustomUser)
def create_account(sender, created, instance, **kwargs):
    if created:
        if instance.account_type == 1:
            Staff.objects.create(user_profile = instance)


@receiver(post_save, sender = CustomUser    )
def save_account(sender, instance, **kwargs):
    if instance.account_type == 1:
        instance.staff.save()