from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.
class Pet(models.Model):
    PET_TYPE_CHOICES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
    ]
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    ADOPTION_STATUS_CHOICES = [
        ('available', 'Available'),
        ('pending', 'Pending'),
    ]

    # add foreign key field to User for the admin who creates the pet
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_type = models.CharField(max_length=10, choices=PET_TYPE_CHOICES, default='dog')
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    weight = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')
    breed = models.CharField(max_length=100)
    adoption_status = models.CharField(max_length=25, choices=ADOPTION_STATUS_CHOICES, default='available')
    description = models.TextField(max_length=500)


    def __str__(self):
        return self.name

    # Handle redirecting for update and create
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pet_id':self.id})



# DEFINE THE PHOTO MODEL (ONE-TO-MANY, ONE PET CAN HAVE MANY PHOTOS)
class Photo(models.Model):
    url = models.CharField(max_length=200)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for pet_id: {self.pet_id}@{self.url}"