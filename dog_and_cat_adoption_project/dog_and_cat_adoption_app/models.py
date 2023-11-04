from django.db import models

# Create your models here.
class Pet(models.Model):
    PET_TYPE_CHOICES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
    ]
    
    pet_type = models.CharField(max_length=10, choices=PET_TYPE_CHOICES, default='dog')
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    weight = models.CharField(max_length=20)

    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')
    breed = models.CharField(max_length=100)

    ADOPTION_STATUS_CHOICES = [
        ('available', 'Available'),
        ('pending', 'Pending'),
    ]

    adoption_status = models.CharField(max_length=25, choices=ADOPTION_STATUS_CHOICES, default='available')
    description = models.TextField(max_length=500)


    def __str__(self):
        return self.name