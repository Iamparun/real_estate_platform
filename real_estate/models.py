from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
class Property(models.Model):
    PROPERTY_TYPE_CHOICES = (
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('land', 'Land'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES)
    listed_date = models.DateTimeField(auto_now_add=True)
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='properties')
    image = models.ImageField(upload_to='property_images/', blank=True, null=True)
    available = models.BooleanField(default=True)  # New field to indicate availability
    buyer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='purchases')
    contact_number = models.CharField(max_length=15, blank=True, null=True)  # New field for contact number

    def __str__(self):
        return self.title

