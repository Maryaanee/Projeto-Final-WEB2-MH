from django.db import models
from django.contrib.auth.models import User

class Filme(models.Model):
    titulo = models.CharField(max_length=100)       # Texto (VARCHAR)
    sinopse = models.CharField(max_length=500)        # Texto (VARCHAR)
    duracao = models.IntegerField()                 # Número Inteiro
    data_lancamento = models.DateField()

    def __str__(self):
        return self.titulo
    
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    foto = models.ImageField(upload_to='perfis/', null=True, blank=True)
    email_confirmado = models.BooleanField(default=False)

    
    def __str__(self):
        return f"Perfil de {self.user.username}"