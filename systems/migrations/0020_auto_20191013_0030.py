# Generated by Django 2.2.3 on 2019-10-13 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0019_auto_20191013_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_impacto_potencial',
            name='impacto_Potencial',
            field=models.CharField(max_length=255, verbose_name='Consequência Causada Por Indisponibilidade'),
        ),
    ]
