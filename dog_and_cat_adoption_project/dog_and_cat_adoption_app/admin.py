from django.contrib import admin
from .models import Pet, Photo

# Register your models here.

admin.site.register(Pet)

# register Photo model
admin.site.register(Photo)
