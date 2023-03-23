# Generated by Django 4.1.7 on 2023-03-23 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id_aluno', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=250)),
                ('matricula', models.CharField(max_length=250, unique=True)),
                ('email', models.EmailField(max_length=250)),
                ('telefone', models.CharField(max_length=250)),
            ],
        ),
    ]
