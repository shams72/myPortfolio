from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone= models.CharField(max_length=200)
    email = models.CharField(max_length=200)    
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ' ' + self.phone + ' ' + self.email + ' ' + self.description  