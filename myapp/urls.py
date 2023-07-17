from django.urls import path
from . import views


#URL configuration 
"""
Now we need to import this url configuration into the main url configuration
for this project
"""
urlpatterns = [
    path('', views.index, name='home'),
    path('scan/', views.home, name='home'),
    path('list/', views.list, name='home')
    
]

