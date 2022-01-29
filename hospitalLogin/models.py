from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from django.db import models

# Create your models here.

class User(models.Model):

    firstName = models.CharField(max_length=50, default='')
    lastName = models.CharField(max_length=50, default='')
    profilePicture = models.ImageField(upload_to = 'uploads/', default='')
    username = models.CharField(max_length=50, primary_key=True)
    emailId = models.EmailField(default='')
    password = models.CharField(max_length=20, default='')
    confirmPassword = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=200, default='')
    user = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.username