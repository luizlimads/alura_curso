from django.db import models
from datetime import datetime
from pessoas.models import Pessoa

class Receita(models.Model):
    pessoas = models.ForeignKey(Pessoa, on_delete= models.CASCADE)
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    date_receita = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.nome_receita
# Create your models here.