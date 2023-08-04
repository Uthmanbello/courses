from django.contrib import admin

# Register your models here.
from .models import Courselist, Topic
admin.site.register(Courselist)
admin.site.register(Topic)
