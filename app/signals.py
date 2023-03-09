from .models import *
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=User)
def create_user_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user_profile = instance)
