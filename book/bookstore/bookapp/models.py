from django.db import models
class Book(models.Model):
    bookname=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    price=models.IntegerField()
    qty=models.IntegerField()
    publisher=models.CharField(max_length=200)

    def __str__(self):
        return self.bookname


# Create your models here.
