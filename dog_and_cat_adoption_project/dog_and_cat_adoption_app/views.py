from django.shortcuts import render, redirect
from .models import Pet, Photo
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

## imports for photo aws
import uuid
import boto3
## to access .env key
import os
import logging


# pets = [
#   {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
#   {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
# ]


# CREATE YOUR VIEWS HERE | THESE ARE VIEW FUNCTIONS
def home(request):
    return render(request, 'dogncat/home.html')

def about(request):
    return render(request, 'dogncat/about.html')  

def contact(request):
    return render(request, 'dogncat/contact.html')

def hours_locations(request):
    return render(request, 'dogncat/hours_locations.html')


# def pets_index(request):
#     pets = Pet.objects.all()

#     # Handle sorting
#     sort_by = request.GET.get('sort_by', 'name')  # Default to sorting by name
#     pets = pets.order_by(sort_by)

#     context = {'pet': pets}

#     return render(request, 'dogncat/index.html', context)
def pets_index(request):
    sort_by = request.GET.get('sort_by', 'name')
    if sort_by == '':
        sort_by = 'name'
    pets = Pet.objects.all().order_by(sort_by)
    return render(request, 'dogncat/index.html', {'pet': pets})


###### ADD ######
def dog_list(request):
    sort_by_options = ['name', 'gender', 'breed']
    sort_by = request.GET.get('sort_by', 'name')    # Default to sorting by name

    if sort_by not in sort_by_options:
        sort_by = 'name' 

    
    dogs = Pet.objects.filter(pet_type='dog').order_by(sort_by)

    context = {'dog': dogs}
    return render(request, 'dogncat/dog_list.html', context)



def cat_list(request):
    sort_by_options = ['name', 'gender', 'breed']
    sort_by = request.GET.get('sort_by', 'name')  # Default to sorting by name

    if sort_by not in sort_by_options:
        sort_by = 'name'
    
    cats = Pet.objects.filter(pet_type='cat').order_by(sort_by)

    context = {'cat': cats}
    return render(request, 'dogncat/cat_list.html', context)
###### END ADD ######





def pets_detail(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    return render(request, 'dogncat/detail.html', {'pet' : pet})


## DEFINE THE ADD PHOTO VIEW
def add_photo(request, pet_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"

            logging.info(f"Successfully uploaded photo to S3. URL: {url}")

            Photo.objects.create(url=url, pet_id=pet_id)
        except Exception as e:
            logging.error('An error occurred uploading file to S3')
            logging.error(e)
            return HttpResponse(status=500)
        return redirect('detail', pet_id=pet_id)



# CLASS BASED VIEWS
class PetCreate(CreateView):
    model = Pet
    fields = ['pet_type', 'name', 'age', 'weight', 'gender', 'breed', 'adoption_status', 'description']

    # inherited (built-in) method is called a valid pet form is being submitted
    def form_valid(self, form):
        # assign the logged in user (self.request.user)
        form.instance.user = self.request.user
        return super().form_valid(form)






class PetUpdate(UpdateView):
    model = Pet
    fields = ['pet_type', 'name', 'age', 'weight', 'gender', 'breed', 'adoption_status', 'description']


class PetDelete(DeleteView):
    model = Pet
    success_url = '/pets/'
