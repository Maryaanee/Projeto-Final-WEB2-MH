from django.urls import path
from . import views 

urlpatterns = [
    
    path('signup/', views.cadastrar, name='signup'),
]