from django.core.mail import send_mail
from .models import User


def notify_admins(message):
    admins = User.objects.filter(is_admin=True)
    for admin in admins:
        send_mail(
            'Product Update Notification',
            message,
            'no-reply@zebrands.com',
            [admin.email],
            fail_silently=True,
        )
