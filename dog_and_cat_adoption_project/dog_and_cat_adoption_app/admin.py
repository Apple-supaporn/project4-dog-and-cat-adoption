from django.contrib import admin
from .models import Pet, Photo

# Register your models

## Register Pet model ##
admin.site.register(Pet)

## Register Photo model ##
admin.site.register(Photo)
