# Generated by Django 2.2.3 on 2019-12-19 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0005_auto_20191219_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_infraestrutura',
            name='camada_aplicacao',
            field=models.CharField(max_length=255, verbose_name='Descreva brevemente a estrutura da camada de Aplicação:'),
        ),
        migrations.AlterField(
            model_name='t_infraestrutura',
            name='camada_balanceador',
            field=models.CharField(max_length=255, verbose_name='Descreva brevemente a estrutura da camada de Balanceador:'),
        ),
        migrations.AlterField(
            model_name='t_infraestrutura',
            name='camada_banco_dados',
            field=models.CharField(max_length=255, verbose_name='Descreva brevemente a estrutura da camada de Banco de Dados:'),
        ),
    ]