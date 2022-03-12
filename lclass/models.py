from unicodedata import name
from django.db import models
from acc.models import User
# Create your models here.

class Job(models.Model):
    name=models.CharField(max_length=100)
    ones=models.TextField(default='')
    content=models.TextField()
    iden=models.TextField()
    root=models.CharField(max_length=100, default='')
    pic=models.ImageField(upload_to="lclass/%y")
    likey=models.ManyToManyField(User,blank=True)
    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/media/익명이.png"
    def __str__(self):
        return self.name 

class Reply(models.Model):
    board=models.ForeignKey(Job, on_delete=models.CASCADE)
    replyer=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField()
    def __str__(self):
        return f"{self.board}_{self.replyer}"
    
    