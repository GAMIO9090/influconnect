from django.db import models

# Create your models here.



class Influencer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    niche = models.CharField(max_length=50)
    followers = models.IntegerField()
    instagram = models.URLField()
    price = models.IntegerField()
    bio = models.TextField()

    def __str__(self):
        return self.name
