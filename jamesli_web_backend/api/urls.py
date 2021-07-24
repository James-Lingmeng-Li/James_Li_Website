from django.urls import path
from .views import main

urlpatterns = [
    path('homehome', main),
    path('', main)
    
]