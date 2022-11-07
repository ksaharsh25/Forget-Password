from django.db import models

# Create your models here.
class Email(models.Model):
    email=models.EmailField(max_length=50,blank=False,null=False)
    password=models.CharField(max_length=100,blank=False,null=False)
    forget_password_token=models.CharField(max_length=50,blank=True)
    