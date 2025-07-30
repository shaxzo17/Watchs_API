from django.db import models

# Create your models here.
class Watch(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=70)
    color = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    image = models.ImageField(upload_to='watch_images/')

    def __str__(self):
        return self.name