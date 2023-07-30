from django.db import models

# Create your models here.
class Courselist(models.Model):
    name = models.CharField(max_length=100)
    ICON_CHOICES = [
        ('icon1', 'Icon 1'),
        ('icon2', 'Icon 2'),
        ('icon3', 'Icon 3'),
        # Add more choices here as needed
    ]
    icon = models.CharField(max_length=20, choices=ICON_CHOICES, default='default_icon')