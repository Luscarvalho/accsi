from django.db import models


class Aluno(models.Model):
    id_aluno = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    matricula = models.IntegerField(max_length=8, unique=True)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=20)
