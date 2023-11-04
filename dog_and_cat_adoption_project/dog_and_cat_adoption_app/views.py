from django.shortcuts import render
from .models import Pet
#from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView



# pets = [
#   {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
#   {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
# ]


# CREATE YOUR VIEWS HERE | THESE ARE VIEW FUNCTIONS
def home(request):
    return render(request, 'dogncat/home.html')

def about(request):
    return render(request, 'dogncat/about.html')  


def pets_index(request):
    pets = Pet.objects.all()
    return render(request, 'dogncat/index.html', {'pet' : pets}) 

def pets_detail(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    return render(request, 'dogncat/detail.html', {'pet' : pet})


# CLASS BASED VIEWS
class PetCreate(CreateView):
    model = Pet
    fields = '__all__'


class PetUpdate(UpdateView):
    model = Pet
    fields = ['pet_type', 'name', 'age', 'weight', 'gender', 'breed', 'adoption_status', 'description']


class PetDelete(DeleteView):
    model = Pet
    succes_url = '/pets'
