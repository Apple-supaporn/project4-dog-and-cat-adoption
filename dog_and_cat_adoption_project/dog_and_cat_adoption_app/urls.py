from django.urls import path
from . import views     # .  is everything from views



urlpatterns = [
    path('', views.home, name='home'),  # name='home' is kwarg (key of name and a value of home)
    path('about/', views.about, name='about'),
    path('pets/', views.pets_index, name="index"),
    path('pets/<int:pet_id>/', views.pets_detail, name='detail'),
    path('pets/create/', views.PetCreate.as_view(), name='pets_create'),
    path('pets/<int:pk>/update/', views.PetUpdate.as_view(), name='pets_update'),
    path('pets/<int:pk>/delete/', views.PetDelete.as_view(), name='pets_delete'),



    # path('pets/', views.pets, name='index'),
]