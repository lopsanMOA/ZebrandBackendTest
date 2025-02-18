from django.contrib.auth.models import AbstractUser
from django.db import models
from users.utils import notify_admins



class Product(models.Model):
    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=255)
    query_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.pk:
            pass
            #notify_admins(f'Product {self.name} was updated.')
        super().save(*args, **kwargs)
