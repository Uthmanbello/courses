from django.db import models

# Create your models here.
class Courselist(models.Model):
    name = models.CharField(max_length=100)
    ICON_CHOICES = [
        ('python', 'python'),
        ('javascript', 'javascript'),
        ('c', 'c'),
        ('css', 'css'),
        ('java', 'java'),
        ('swift', 'swift'),
        ('scala', 'scala'),
        ('kotlin', 'kotlin'),
        ('php', 'php'),
        ('ruby', 'ruby'),
        ('rust', 'rust'),
        ('html', 'html'),
        ('default', 'default'),
    ]
    icon = models.CharField(max_length=20, choices=ICON_CHOICES, default='default')

class Topic(models.Model):
    course = models.ForeignKey(Courselist, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField(max_length=30)
    note = models.TextField(default='N/A')
    duration = models.IntegerField(default=0)