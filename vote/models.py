from django.db import models
from acc.models import User

# Create your models here.

class Topic(models.Model):
    subject=models.CharField(max_length=100)
    maker=models.ForeignKey(User,on_delete=models.CASCADE, related_name="maker")
    content=models.TextField()
    voter=models.ManyToManyField(User,blank=True, related_name="voter")
    def __str__(self):
        return self.subject

class Choice(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    chname=models.CharField(max_length=100)
    chnum=models.IntegerField(default=0)
    def __str__(self):
        return f"{self.topic}_{self.chname}"

class Reply(models.Model):
    board=models.ForeignKey(Topic, on_delete=models.CASCADE)
    replyer=models.ForeignKey(User,on_delete=models.CASCADE,related_name="Topic_replyer")
    comment=models.TextField()
    def __str__(self):
        return f"{self.board}_{self.replyer}"