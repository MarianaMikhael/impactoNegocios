# Generated by Django 2.2.3 on 2019-10-13 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0003_auto_20191012_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_sistema',
            name='fk_Responsavel_Dev',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Responsavel_Desenvolvimento', verbose_name='Área de Desenvolvimento'),
        ),
        migrations.AlterField(
            model_name='t_sistema',
            name='fk_Responsavel_Sup',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Responsavel_Suporte', verbose_name='Área de Suporte'),
        ),
    ]
