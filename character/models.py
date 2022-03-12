from django.db import models
from acc.models import User
# Create your models here.

class Character(models.Model):
    board=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=12)
    level=models.FloatField()
    job=models.CharField(max_length=100)
    pic=models.ImageField(upload_to="character/%y")
    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/media/익명이.png"
    def __str__(self):
        return f"{self.board}_{self.name}"