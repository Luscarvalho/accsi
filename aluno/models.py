from django.db import models


class Aluno(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    matricula = models.IntegerField(unique=True)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=20)
