from django.shortcuts import render
from .models import Pet
#from django.http import HttpResponse










# Create your views here.
def home(request):
    return render(request, 'pets/home.html')

def about(request):
    return render(request, 'pets/about.html')  


def pets(request):
    pets = Pet.object.all()
    return render(request, 'pets/pets_index.html', {'pets' : pets}) 
