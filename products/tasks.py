from __future__ import absolute_import, unicode_literals
from zebrands.celery import app
from celery import shared_task
from django.core.mail import send_mail
from users.models import User
from django.conf import settings


@shared_task
def send_email_notification(message):
    admins = User.objects.filter(is_admin=True).values_list('email', flat=True)
    try:
        send_mail(
            'Product Update Notification',
            message,
            settings.EMAIL_HOST_USER,
            admins,
        )
        print("hola")
    except Exception as e:
        print(e.args)
