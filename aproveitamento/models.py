from django.db import models
from aluno.models import Aluno
from atividade.models import Atividade


class Aproveitamento(models.Model):
    id_aproveitamento = models.AutoField(primary_key=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=250)
    categoria = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    semestre = models.IntegerField(max_length=1)
    ano = models.IntegerField(max_length=4)
    ch = models.IntegerField(max_length=3)
