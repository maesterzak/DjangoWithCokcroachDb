from django.urls import path
from .views import *



app_name = "dashboard"
urlpatterns = [
    path('', homepage, name='homepage'),
    #profile
    path('profile/', profile, name='profile'),
    
    
]