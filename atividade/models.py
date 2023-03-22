from django.db import models
from modalidade.models import Modalidade


class Atividade(models.Model):
    id_atividade = models.AutoField(primary_key=True)
    codigo = models.CharField(unique=True, max_length=10)
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE)
    nome = models.CharField(max_length=250, null=False)
    descricao = models.CharField(max_length=250, unique=True)
    ch_min = models.CharField(max_length=250, null=False)
    ch_max = models.CharField(max_length=250, null=False)
    ap_max = models.CharField(max_length=250, null=False)

    def __str__(self):
        return self.codigo
