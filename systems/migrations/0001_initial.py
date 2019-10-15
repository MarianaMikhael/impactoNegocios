# Generated by Django 2.2.3 on 2019-10-15 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='t_Area_Desenvolvimento',
            fields=[
                ('cod_Area_Dev', models.AutoField(primary_key=True, serialize=False)),
                ('area_Dev', models.CharField(max_length=128, verbose_name='Área')),
                ('gerente_Area_Dev', models.CharField(blank=True, max_length=128, verbose_name='Gerente')),
                ('coordenador_Area_Dev', models.CharField(blank=True, max_length=128, verbose_name='Coordenador')),
            ],
            options={
                'verbose_name': 'Área de Desenvolvimento',
                'verbose_name_plural': 'Áreas de Desenvolvimento',
            },
        ),
        migrations.CreateModel(
            name='t_Area_Suporte',
            fields=[
                ('cod_Area_Sup', models.AutoField(primary_key=True, serialize=False)),
                ('area_Sup', models.CharField(max_length=128, verbose_name='Área')),
                ('gerente_Area_Sup', models.CharField(blank=True, max_length=128, verbose_name='Gerente')),
                ('coordenador_Area_Sup', models.CharField(blank=True, max_length=128, verbose_name='Coordenador')),
            ],
            options={
                'verbose_name': 'Área de Suporte',
                'verbose_name_plural': 'Áreas de Suporte',
            },
        ),
        migrations.CreateModel(
            name='t_Cadeia_Servico',
            fields=[
                ('cod_Cadeia_Servico', models.AutoField(primary_key=True, serialize=False)),
                ('cadeia_Servico', models.CharField(max_length=128, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Cadeia de Serviço',
                'verbose_name_plural': 'Cadeia de Serviço',
            },
        ),
        migrations.CreateModel(
            name='t_Contingencia',
            fields=[
                ('cod_Contingencia', models.AutoField(primary_key=True, serialize=False)),
                ('contingencia_Arquitetura', models.CharField(choices=[('', ''), ('S', 'Sim'), ('N', 'Não'), ('C', 'À Confirmar')], default='', max_length=1, verbose_name='Contingenciado pela Arquitetura TecBan?')),
                ('contingencia_Usuario', models.CharField(choices=[('', ''), ('S', 'Sim'), ('N', 'Não'), ('C', 'À Confirmar')], default='', max_length=1, verbose_name='Contingenciado pelo Usuário?')),
                ('RTO_Contingencia', models.DecimalField(blank=True, decimal_places=2, max_digits=4, verbose_name='RTO(hrs) Contingência')),
            ],
            options={
                'verbose_name': 'Contingência',
                'verbose_name_plural': 'Contingências',
            },
        ),
        migrations.CreateModel(
            name='t_Continuidade_Tecnologica',
            fields=[
                ('cod_Continuidade', models.AutoField(primary_key=True, serialize=False)),
                ('continuidade_Tecnologica', models.CharField(choices=[('', ''), ('DR', 'Disaster Recovery'), ('AD', 'Alta Disponibilidade')], default='', max_length=2, verbose_name='Continuidade Tecnológica')),
                ('plano_De_Recup_Doc', models.CharField(choices=[('', ''), ('S', 'Sim'), ('N', 'Não'), ('C', 'À Confirmar')], default='', max_length=1, verbose_name='Possui plano de recuperação documentado?')),
                ('plano_De_Recup_Test', models.CharField(choices=[('', ''), ('S', 'Sim'), ('N', 'Não'), ('C', 'À Confirmar')], default='', max_length=1, verbose_name='Possui plano de recuperação testado?')),
                ('url_Ficheiro', models.URLField(blank=True, max_length=250, verbose_name='URL - Documentação')),
            ],
            options={
                'verbose_name': 'Continuidade Tecnológica',
                'verbose_name_plural': 'Continuidade Tecnológica',
            },
        ),
        migrations.CreateModel(
            name='t_Criticidade',
            fields=[
                ('cod_Criticidade', models.AutoField(primary_key=True, serialize=False)),
                ('nivel_Criticidade', models.CharField(choices=[('', ''), ('AC', 'AC'), ('ACN', 'ACN'), ('ACN+', 'ACN+')], default='', max_length=4, verbose_name='Nível de Criticidade')),
                ('criticidade_Suporte', models.CharField(choices=[('', ''), ('Não Aplicável', 'Não Aplicável'), ('Não Crítico', 'Não Crítico'), ('Importante', 'Importante'), ('Crítico', 'Crítico'), ('Missão Crítica', 'Missão Crítica'), ('Infraestrutura', 'Infraestrutura')], default='', max_length=14, verbose_name='Criticidade Suporte')),
            ],
            options={
                'verbose_name': 'Nível de Criticidade',
                'verbose_name_plural': 'Nível de Criticidade',
            },
        ),
        migrations.CreateModel(
            name='t_Impacto_Dependencia',
            fields=[
                ('cod_Dependencia', models.AutoField(primary_key=True, serialize=False)),
                ('dependencia', models.CharField(blank=True, max_length=128, verbose_name='Nome da Aplicação Dependente')),
            ],
            options={
                'verbose_name': 'Impacto (Dependência)',
                'verbose_name_plural': 'Impactos (Dependências)',
            },
        ),
        migrations.CreateModel(
            name='t_Impacto_Fronteira',
            fields=[
                ('cod_Fronteira', models.AutoField(primary_key=True, serialize=False)),
                ('fronteira', models.CharField(blank=True, max_length=128, verbose_name='Nome da Aplicação Que Faz Fronteira')),
            ],
            options={
                'verbose_name': 'Impacto (Fronteira)',
                'verbose_name_plural': 'Impactos (Fronteiras)',
            },
        ),
        migrations.CreateModel(
            name='t_Impacto_Potencial',
            fields=[
                ('cod_Impacto_Potencial', models.AutoField(primary_key=True, serialize=False)),
                ('impacto_Potencial', models.CharField(max_length=255, verbose_name='Consequência Causada Por Indisponibilidade')),
            ],
            options={
                'verbose_name': 'Impacto Potencial',
                'verbose_name_plural': 'Impactos Potenciais',
            },
        ),
        migrations.CreateModel(
            name='t_Impacto_Usuario',
            fields=[
                ('cod_Usuario_Chave', models.AutoField(primary_key=True, serialize=False)),
                ('usuario_Chave', models.CharField(max_length=128, verbose_name='Usuário Chave')),
            ],
            options={
                'verbose_name': 'Impacto (Usuário Chave)',
                'verbose_name_plural': 'Impactos (Usuários Chave)',
            },
        ),
        migrations.CreateModel(
            name='t_Responsavel_Desenvolvimento',
            fields=[
                ('cod_Responsavel_Dev', models.AutoField(primary_key=True, serialize=False)),
                ('celula_Dev', models.CharField(blank=True, max_length=128, verbose_name='Célula de Desenvolvimento')),
                ('nome_Resp_Dev', models.CharField(blank=True, max_length=128, verbose_name='Desenvolvedor Responsável')),
                ('fk_Area_Dev', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Area_Desenvolvimento', verbose_name='Área')),
            ],
            options={
                'verbose_name': 'Responsável pelo Desenvolvimento',
                'verbose_name_plural': 'Responsáveis pelo Desenvolvimento',
            },
        ),
        migrations.CreateModel(
            name='t_Responsavel_Suporte',
            fields=[
                ('cod_Responsavel_Sup', models.AutoField(primary_key=True, serialize=False)),
                ('celula_Sup', models.CharField(blank=True, max_length=128, verbose_name='Célula de Sustentação')),
                ('nome_Resp_Sup', models.CharField(blank=True, max_length=128, verbose_name='Sustentador Responsável')),
                ('fk_Area_Sup', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Area_Suporte', verbose_name='Área')),
            ],
            options={
                'verbose_name': 'Responsável pelo Suporte',
                'verbose_name_plural': 'Responsáveis pelo Suporte',
            },
        ),
        migrations.CreateModel(
            name='t_Sistema_Janelas',
            fields=[
                ('cod_Janela', models.AutoField(primary_key=True, serialize=False)),
                ('janela_Critica', models.CharField(max_length=128, verbose_name='Período')),
            ],
            options={
                'verbose_name': 'Sistema (Janela Crítica)',
                'verbose_name_plural': 'Sistemas (Janelas Críticas)',
            },
        ),
        migrations.CreateModel(
            name='t_Sistema_Servico',
            fields=[
                ('cod_Servico', models.AutoField(primary_key=True, serialize=False)),
                ('servico', models.CharField(blank=True, max_length=255, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Sistema (Serviço)',
                'verbose_name_plural': 'Sistemas (Serviços)',
            },
        ),
        migrations.CreateModel(
            name='t_Sistema',
            fields=[
                ('cod_Sistema', models.AutoField(primary_key=True, serialize=False)),
                ('sistema', models.CharField(max_length=128, verbose_name='Sistema')),
                ('RTO_hrs', models.DecimalField(blank=True, decimal_places=2, max_digits=4, verbose_name='RTO(hrs)')),
                ('servidores', models.CharField(blank=True, max_length=128, verbose_name='Servidores')),
                ('url_Topologia', models.URLField(blank=True, max_length=250, verbose_name='URL - Topologia')),
                ('fk_Cadeia_Servico', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Cadeia_Servico', verbose_name='Cadeia de Serviço')),
                ('fk_Criticidade', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Criticidade', verbose_name='Criticidade')),
                ('fk_Responsavel_Dev', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Responsavel_Desenvolvimento', verbose_name='Célula de Desenvolvimento')),
                ('fk_Responsavel_Sup', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Responsavel_Suporte', verbose_name='Célula de Sustentação')),
                ('janelas_Criticas', models.ManyToManyField(to='systems.t_Sistema_Janelas', verbose_name='Janelas Críticas')),
                ('servicos', models.ManyToManyField(to='systems.t_Sistema_Servico', verbose_name='Serviço')),
            ],
            options={
                'verbose_name': 'Sistema',
                'verbose_name_plural': 'Sistemas',
            },
        ),
        migrations.CreateModel(
            name='t_Impacto',
            fields=[
                ('cod_Impacto', models.AutoField(primary_key=True, serialize=False)),
                ('cliente', models.CharField(choices=[('', ''), ('Int', 'Internos'), ('Ext', 'Externos'), ('Ambos', 'Ambos')], default='', max_length=5, verbose_name='Impacta clientes:')),
                ('perda_Receita', models.CharField(choices=[('', ''), ('D', 'Direto'), ('I', 'Indireto'), ('N/A', 'Sem Impacto')], default='', max_length=3, verbose_name='Gera perda de receita?')),
                ('despesas_Adicionais', models.CharField(choices=[('', ''), ('D', 'Direto'), ('I', 'Indireto'), ('N/A', 'Sem Impacto')], default='', max_length=3, verbose_name='Gera despesas adicionais?')),
                ('elevacao_Custo_Transacional', models.CharField(choices=[('', ''), ('D', 'Direto'), ('I', 'Indireto'), ('N/A', 'Sem Impacto')], default='', max_length=3, verbose_name='Gera elevação do custo transacional?')),
                ('afeta_Disponibilidade', models.CharField(choices=[('', ''), ('D', 'Direto'), ('I', 'Indireto'), ('N/A', 'Sem Impacto')], default='', max_length=3, verbose_name='Afeta a disponibilidade?')),
                ('afeta_Imagem_IF', models.CharField(choices=[('', ''), ('D', 'Direto'), ('I', 'Indireto'), ('N/A', 'Sem Impacto')], default='', max_length=3, verbose_name='Afeta a imagem da Tecban com as IFs?')),
                ('afeta_Imagem_Consumidor', models.CharField(choices=[('', ''), ('D', 'Direto'), ('I', 'Indireto'), ('N/A', 'Sem Impacto')], default='', max_length=3, verbose_name='Afeta a imagem da TecBan com o consumidor final?')),
                ('impacto_Operacional', models.CharField(choices=[('', ''), ('D', 'Direto'), ('I', 'Indireto'), ('N/A', 'Sem Impacto')], default='', max_length=3, verbose_name='Gera impacto operacional?')),
                ('impacto_Adm', models.CharField(choices=[('', ''), ('D', 'Direto'), ('I', 'Indireto'), ('N/A', 'Sem Impacto')], default='', max_length=3, verbose_name='Gera impacto administrativo?')),
                ('impacto_Contratual', models.CharField(choices=[('', ''), ('D', 'Direto'), ('I', 'Indireto'), ('N/A', 'Sem Impacto')], default='', max_length=3, verbose_name='gera impacto contratual?')),
                ('impacto_Legal', models.CharField(choices=[('', ''), ('D', 'Direto'), ('I', 'Indireto'), ('N/A', 'Sem Impacto')], default='', max_length=3, verbose_name='Gera impacto legal?')),
                ('observacoes', models.TextField(blank=True, verbose_name='Observações')),
                ('dependencias', models.ManyToManyField(to='systems.t_Impacto_Dependencia', verbose_name='Dependências')),
                ('fk_Sistema', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Sistema', verbose_name='Sistema')),
                ('fronteiras', models.ManyToManyField(to='systems.t_Impacto_Fronteira', verbose_name='Fronteiras')),
                ('impactos_Potenciais', models.ManyToManyField(to='systems.t_Impacto_Potencial', verbose_name='Impactos Potenciais')),
                ('usuario_Chave', models.ManyToManyField(to='systems.t_Impacto_Usuario', verbose_name='Usuários Chave')),
            ],
            options={
                'verbose_name': 'Impacto',
                'verbose_name_plural': 'Impactos',
            },
        ),
        migrations.CreateModel(
            name='t_Continuidade_Tecnologica_Sites',
            fields=[
                ('cod_Continuidade_Tecnologica', models.AutoField(primary_key=True, serialize=False)),
                ('camada', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15)], verbose_name='Camada de Serviço')),
                ('servico', models.CharField(max_length=128, verbose_name='Serviço')),
                ('site', models.CharField(choices=[('', ''), ('V', 'Vivo'), ('D', 'Diveo'), ('C', 'Cetem')], default='', max_length=1, verbose_name='Site (DataCenter)')),
                ('observacao', models.TextField(blank=True, verbose_name='Observações')),
                ('fk_Continuidade', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Continuidade_Tecnologica', verbose_name='Continuidade Tecnológica')),
            ],
            options={
                'verbose_name': 'Continuidade Tecnológica (Site)',
                'verbose_name_plural': 'Continuidade Tecnológica (Sites)',
            },
        ),
        migrations.AddField(
            model_name='t_continuidade_tecnologica',
            name='fk_Sistema',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Sistema', verbose_name='Sistema'),
        ),
        migrations.CreateModel(
            name='t_Contingencia_Usuario',
            fields=[
                ('cod_Nome', models.AutoField(primary_key=True, serialize=False)),
                ('nome_Contingencia', models.CharField(max_length=128, verbose_name='Nome da Contingência (Usuário)')),
                ('fk_Contingencia', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Contingencia', verbose_name='Sistema Contingenciado')),
            ],
            options={
                'verbose_name': 'Contingência (Usuário)',
                'verbose_name_plural': 'Contingências (Usuário)',
            },
        ),
        migrations.CreateModel(
            name='t_Contingencia_Arquitetura',
            fields=[
                ('cod_Nome', models.AutoField(primary_key=True, serialize=False)),
                ('nome_Contingencia', models.CharField(max_length=128, verbose_name='Nome da Contingência (Arquitetura)')),
                ('fk_Contingencia', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Contingencia', verbose_name='Sistema Contingenciado')),
            ],
            options={
                'verbose_name': 'Contingência (Arquitetura TecBan)',
                'verbose_name_plural': 'Contingências (Arquitetura TecBan)',
            },
        ),
        migrations.AddField(
            model_name='t_contingencia',
            name='fk_Sistema',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Sistema', verbose_name='Sistema'),
        ),
    ]
