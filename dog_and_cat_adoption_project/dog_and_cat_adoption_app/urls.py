from django.urls import path
from . import views     # .  is everything from views



urlpatterns = [
    path('', views.home, name='home'),  # name='home' is kwarg (key of name and a value of home)
    path('about/', views.about, name='about'),
    path('adoption/', views.adoption_index, name="index"),



    # path('pets/', views.pets, name='index'),
]