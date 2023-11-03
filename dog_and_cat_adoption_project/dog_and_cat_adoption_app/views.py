from django.shortcuts import render
#from .models import Pet
#from django.http import HttpResponse






# Create your views here.
def home(request):
    return render(request, 'dogncat/home.html')

def about(request):
    return render(request, 'dogncat/about.html')  


# def pets(request):
#     pets = Pet.object.all()
#     return render(request, 'pets/pets_index.html', {'pets' : pets}) 
