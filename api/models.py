from django.db import models



class Books(models.Model):
    name=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    publication=models.CharField(max_length=200)
    qty=models.PositiveIntegerField(default=1)


    def __str__(self):
        return(self.name)#this fuction is used to print the book name

class Reviews(models.Model):
    book=models.CharField(max_length=200)
    user=models.CharField(max_length=200)
    comment=models.CharField(max_length=200)
    rating=models.PositiveIntegerField()
    created_date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.cmment
