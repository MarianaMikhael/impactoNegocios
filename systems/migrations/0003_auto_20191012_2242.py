# Generated by Django 2.2.3 on 2019-10-13 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0002_auto_20191012_2115'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='t_contingencia',
            name='cod_Sistema',
        ),
        migrations.RemoveField(
            model_name='t_contingencia_arquitetura_nome',
            name='cod_Contingencia',
        ),
        migrations.RemoveField(
            model_name='t_contingencia_usuario_nome',
            name='cod_Contingencia',
        ),
        migrations.RemoveField(
            model_name='t_continuidade_tecnologica',
            name='cod_Sistema',
        ),
        migrations.RemoveField(
            model_name='t_continuidade_tecnologica_sites',
            name='cod_Continuidade',
        ),
        migrations.RemoveField(
            model_name='t_impacto',
            name='cod_Sistema',
        ),
        migrations.RemoveField(
            model_name='t_impacto_usuarios',
            name='cod_Impacto',
        ),
        migrations.RemoveField(
            model_name='t_responsavel_desenvolvimento',
            name='cod_Area_Dev',
        ),
        migrations.RemoveField(
            model_name='t_responsavel_suporte',
            name='cod_Area_Sup',
        ),
        migrations.RemoveField(
            model_name='t_sistema',
            name='cod_Cadeia_Servico',
        ),
        migrations.RemoveField(
            model_name='t_sistema',
            name='cod_Criticidade',
        ),
        migrations.RemoveField(
            model_name='t_sistema',
            name='cod_Responsavel_Dev',
        ),
        migrations.RemoveField(
            model_name='t_sistema',
            name='cod_Responsavel_Sup',
        ),
        migrations.AddField(
            model_name='t_contingencia',
            name='fk_Sistema',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Sistema', verbose_name='Sistema'),
        ),
        migrations.AddField(
            model_name='t_contingencia_arquitetura_nome',
            name='fk_Contingencia',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Contingencia', verbose_name='Contingência'),
        ),
        migrations.AddField(
            model_name='t_contingencia_usuario_nome',
            name='fk_Contingencia',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Contingencia', verbose_name='Contingência'),
        ),
        migrations.AddField(
            model_name='t_continuidade_tecnologica',
            name='fk_Sistema',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Sistema', verbose_name='Sistema'),
        ),
        migrations.AddField(
            model_name='t_continuidade_tecnologica_sites',
            name='fk_Continuidade',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Continuidade_Tecnologica', verbose_name='Continuidade'),
        ),
        migrations.AddField(
            model_name='t_impacto',
            name='fk_Sistema',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Sistema', verbose_name='Sistema'),
        ),
        migrations.AddField(
            model_name='t_impacto_usuarios',
            name='fk_Impacto',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Impacto', verbose_name='Impacto'),
        ),
        migrations.AddField(
            model_name='t_responsavel_desenvolvimento',
            name='fk_Area_Dev',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Area_Desenvolvimento', verbose_name='Célula de Desenvolvimento'),
        ),
        migrations.AddField(
            model_name='t_responsavel_suporte',
            name='fk_Area_Sup',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Area_Suporte', verbose_name='Célula de Suporte'),
        ),
        migrations.AddField(
            model_name='t_sistema',
            name='fk_Cadeia_Servico',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Cadeia_Servico', verbose_name='Cadeia de Serviço'),
        ),
        migrations.AddField(
            model_name='t_sistema',
            name='fk_Criticidade',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Criticidade_Suporte', verbose_name='Criticidade'),
        ),
        migrations.AddField(
            model_name='t_sistema',
            name='fk_Responsavel_Dev',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Responsavel_Desenvolvimento', verbose_name='Célula de Desenvolvimento'),
        ),
        migrations.AddField(
            model_name='t_sistema',
            name='fk_Responsavel_Sup',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Responsavel_Suporte', verbose_name='Célula de Suporte'),
        ),
        migrations.AlterField(
            model_name='t_contingencia',
            name='RTO_Contingencia',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, verbose_name='RTO(hrs) Contingência'),
        ),
    ]
