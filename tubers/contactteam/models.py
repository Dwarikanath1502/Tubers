from django.db import models

# Create your models here.

class Contactteam(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    company_name= models.CharField(max_length=100, blank= True)
    subject= models.CharField(max_length=100)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    
    def __str__(self):
        return self.email
