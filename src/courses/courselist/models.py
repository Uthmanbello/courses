from django.db import models

# Create your models here.
class Courselist(models.Model):
    name = models.CharField(max_length=100)
    ICON_CHOICES = [
        ('icon1', 'Icon 1'),
        ('icon2', 'Icon 2'),
        ('icon3', 'Icon 3'),
    ]
    icon = models.CharField(max_length=20, choices=ICON_CHOICES, default='default_icon')

class Topic(models.Model):
    course = models.ForeignKey(Courselist, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField(max_length=100)
    description = models.TextField()