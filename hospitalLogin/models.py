from distutils.command.upload import upload
from pyexpat import model
from django.db import models

# Create your models here.

class User(models.Model):

    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    profilePicture = models.ImageField(upload_to = 'uploads/')
    username = models.CharField(max_length=50, primary_key=True)
    emailId = models.EmailField()
    password = models.CharField(max_length=20)
    confirmPassword = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.username