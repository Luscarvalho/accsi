from django.db import models


class Aluno(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=250, null=False)
    matricula = models.CharField(max_length=250, unique=True)
    email = models.EmailField(max_length=250, null=False)
    telefone = models.CharField(max_length=250, null=False)
