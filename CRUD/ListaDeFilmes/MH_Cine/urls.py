from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    
    path('cadastrar/', views.cadastrar, name='signup'),

    path('ativar/<str:uidb64>/<str:token>/', views.ativar_conta, name='ativar_conta'),
    
    path('filme/<int:filme_id>/', views.detalhes_filme, name='detalhes_filme'),
]