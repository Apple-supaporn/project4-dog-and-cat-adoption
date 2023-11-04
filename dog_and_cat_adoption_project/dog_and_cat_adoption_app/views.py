from django.shortcuts import render
from .models import Pet
#from django.http import HttpResponse



# pets = [
#   {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
#   {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
# ]


# Create your views here.
def home(request):
    return render(request, 'dogncat/home.html')

def about(request):
    return render(request, 'dogncat/about.html')  


def adoption_index(request):
    pet = Pet.objects.all()
    return render(request, 'dogncat/index.html', {'pet' : pet}) 
