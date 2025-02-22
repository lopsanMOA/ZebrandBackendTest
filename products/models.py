from django.contrib.auth.models import AbstractUser
from django.db import models
from products.tasks import send_email_notification


class Product(models.Model):
    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=255)
    query_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        is_update = self.pk is not None
        super().save(*args, **kwargs)
        if is_update:
            send_email_notification.delay(f'Product {self.name} was updated.')
