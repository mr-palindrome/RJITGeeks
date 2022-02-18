import email

from django.db import models


class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Members(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    email = models.EmailField(max_length=254)
    mobile= models.CharField(max_length=15)
    about = models.TextField(default=None)
    url = models.URLField(max_length=200)
    position= models.ForeignKey(Position,on_delete=models.CASCADE)

    def __str__(self):
        return self.name