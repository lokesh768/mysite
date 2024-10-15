from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import Profile
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=User)
def build_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Food Menu App'
        message = f'Hi {instance.username}, thank you for registering with us!'
        recipient = instance.email

        send_mail(subject,message, settings.DEFAULT_FROM_EMAIL,[recipient], fail_silently=False)
