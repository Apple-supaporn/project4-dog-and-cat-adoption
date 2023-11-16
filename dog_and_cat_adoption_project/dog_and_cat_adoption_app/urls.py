from django.urls import path
from . import views     # .  is everything from views
from .views import dog_list, cat_list, contact, hours_locations, edit_photo



urlpatterns = [
    path('', views.home, name='home'),  # name='home' is kwarg (key of name and a value of home)
    path('about/', views.about, name='about'),
    path('pets/', views.pets_index, name="index"),
    path('pets/<int:pet_id>/', views.pets_detail, name='detail'),
    path('pets/create/', views.PetCreate.as_view(), name='pets_create'),
    path('pets/<int:pk>/update/', views.PetUpdate.as_view(), name='pets_update'),
    path('pets/<int:pk>/delete/', views.PetDelete.as_view(), name='pets_delete'),
    ## url to add photo
    path('pets/<int:pet_id>/add_photo/', views.add_photo, name='add_photo'),

    ##### ADD #####
    path('dogs/', dog_list, name='dog_list'),
    path('cats/', cat_list, name='cat_list'),

    path('contact/', contact, name='contact'),
    path('hours-locations/', hours_locations, name='hours_locations'),

    ### ADD EDIT PHOTO ###
    path('pets/<int:pet_id>/edit_photo/<int:photo_id>/', edit_photo, name='edit_photo'),

    ### ADD DELTE PHOTO ###
    path('pets/<int:pet_id>/delete_photo/<int:photo_id>/', views.delete_photo, name='delete_photo'),

]