from django.db import models

# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    num_bedroom = models.IntegerField()
    num_bathroom = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=200)
    image = models.ImageField()
    
    
    def __str__(self):
        return self.title.title()