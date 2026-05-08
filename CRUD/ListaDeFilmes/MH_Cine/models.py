from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=100)       # Texto (VARCHAR)
    sinopse = models.CharField(max_length=500)        # Texto (VARCHAR)
    duracao = models.IntegerField()                 # Número Inteiro
    data_lancamento = models.DateField()

    def __str__(self):
        return self.titulo