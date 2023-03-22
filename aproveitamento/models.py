from django.db import models
from aluno.models import Aluno
from atividade.models import Atividade


class Aproveitamento(models.Model):
    id_aproveitamento = models.AutoField(primary_key=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=50, null=False)
    categoria = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    semestre = models.CharField(max_length=50, null=False)
    ano = models.CharField(max_length=50, null=False)
    ch = models.CharField(max_length=50, null=False)
