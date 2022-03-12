from django.contrib import admin
from .models import User
from lclass.models import Job,Reply
from vote.models import Topic,Choice

# Register your models here.

admin.site.register(User)
admin.site.register(Job)
admin.site.register(Reply)
admin.site.register(Topic)
admin.site.register(Choice)
