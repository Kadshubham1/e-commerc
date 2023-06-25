from django.db import models

# Create your models here.
class ecomm(models.Model):
    UserName = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    phone= models.IntegerField(default=0)
    
    #this function is used converting object into string
    # def __str__(self) -> str:
    #     return self.Firstname
    
