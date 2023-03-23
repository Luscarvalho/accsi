from django.db import models
from modalidade.models import Modalidade


class Atividade(models.Model):
    id_atividade = models.AutoField(primary_key=True)
    codigo = models.CharField(unique=True, max_length=5)
    modalidade = models.ForeignKey(Modalidade, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=250)
    ch_min = models.IntegerField()
    ch_max = models.IntegerField()
    ap_max = models.IntegerField()

    def __str__(self):
        return self.codigo
