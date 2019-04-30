from django.db import models

# Create your models here.

class Exmodel(models.Model):
    title= models.CharField(max_length=100,blank=True)
    content=models.TextField()
    create=models.DateTimeField(auto_now_add=True)
    
