from django.db import models
from categoria_heroi.models import Categoria
from habilidades.models import Habilidade
from universos.models import Universo


class Heroi(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    habilidade = models.ManyToManyField(Habilidade, related_name='hab_heroi')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria_heroi')
    universo = models.ForeignKey(Universo, on_delete=models.CASCADE, related_name='uni_heroi')

    def __str__(self):
        return self.nome