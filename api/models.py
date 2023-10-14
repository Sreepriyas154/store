from django.db import models
from django.contrib.auth.models import User


class Books(models.Model):
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    publication=models.CharField(max_length=200)
    qty=models.PositiveIntegerField(default=1)


    def __str__(self):
        return(self.name)#this fuction is used to print the book name

class Reviews(models.Model):
    book=models.ForeignKey(Books,on_delete=models.CASCADE)#one to many use foreignkey
    user=models.ForeignKey(User,on_delete=models.CASCADE)#1tomn
    comment=models.CharField(max_length=200)
    rating=models.PositiveIntegerField()
    created_date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.comment
