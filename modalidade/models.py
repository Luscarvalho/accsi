from django.db import models


class Modalidade(models.Model):
    id_modalidade = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome
