from django.db import models

# Create your models here.
class Product(models.Model):
    UNITS = (
        ('OZ', 'Ounce'),
    )

    product = models.CharField(max_length=255, primary_key=True)
    price = models.DecimalField(decimal_places=2, max_digits=50)

    unit = models.CharField(max_length=255)

    store = models.CharField(max_length=255)

