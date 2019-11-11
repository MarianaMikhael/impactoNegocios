# Generated by Django 2.2.3 on 2019-11-11 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
            name='t_Contingencia_Usuario',
            fields=[
                ('cod_Nome', models.AutoField(primary_key=True, serialize=False)),
                ('nome_Contingencia', models.CharField(max_length=128, verbose_name='Nome da Contingência')),
            ],
            options={
                'verbose_name': 'Contingência do Usuário',
                'verbose_name_plural': 'Contingências do Usuário',
            },
        ),
        migrations.CreateModel(
            name='t_Impacto_Direto',
            fields=[
                ('cod_Imp_Direto', models.AutoField(primary_key=True, serialize=False)),
                ('impacto_Direto', models.CharField(blank=True, max_length=128, verbose_name='Serviço Impactado Diretamente')),
            ],
            options={
                'verbose_name': 'Impacto Direto',
                'verbose_name_plural': 'Impactos Diretos',
            },
        ),
        migrations.CreateModel(
            name='t_Impacto_Indireto',
            fields=[
                ('cod_Imp_Indireto', models.AutoField(primary_key=True, serialize=False)),
                ('impacto_Indireto', models.CharField(blank=True, max_length=128, verbose_name='Serviço Impactado Indiretamente')),
            ],
            options={
                'verbose_name': 'Impacto Indireto',
                'verbose_name_plural': 'Impactos Indiretos',
            },
        ),
        migrations.CreateModel(
            name='t_Impacto_Potencial',
            fields=[
                ('cod_Impacto_Potencial', models.AutoField(primary_key=True, serialize=False)),
                ('impacto_Potencial', models.CharField(max_length=255, verbose_name='Consequência Causada Por Indisponibilidade Sistêmica')),
            ],
            options={
                'verbose_name': 'Impacto Potencial',
                'verbose_name_plural': 'Impactos Potenciais',
            },
        ),
        migrations.CreateModel(
            name='t_Responsavel_Desenvolvimento',
            fields=[
                ('cod_Responsavel_Dev', models.AutoField(primary_key=True, serialize=False)),
                ('area_Dev', models.CharField(max_length=128, verbose_name='Área de Desenvolvimento')),
                ('nome_Resp_Area', models.CharField(max_length=128, verbose_name='Responsável Pela Área')),
                ('celula_Dev', models.CharField(blank=True, max_length=128, verbose_name='Célula de Desenvolvimento')),
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
                ('area_Sup', models.CharField(max_length=128, verbose_name='Área de Suporte')),
                ('nome_Resp_Area', models.CharField(max_length=128, verbose_name='Responsável Pela Área')),
                ('celula_Sup', models.CharField(blank=True, max_length=128, verbose_name='Célula de Suporte')),
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
                'verbose_name': 'Janela Crítica',
                'verbose_name_plural': 'Janelas Críticas',
            },
        ),
        migrations.CreateModel(
            name='t_Usuario_Chave',
            fields=[
                ('cod_Usuario_Chave', models.AutoField(primary_key=True, serialize=False)),
                ('area_Usuario', models.CharField(max_length=128, verbose_name='Área do Usuário')),
                ('usuario_Chave', models.CharField(max_length=128, verbose_name='Usuário Chave')),
            ],
            options={
                'verbose_name': 'Usuário Chave',
                'verbose_name_plural': 'Usuários Chave',
            },
        ),
        migrations.CreateModel(
            name='t_Sistema',
            fields=[
                ('cod_Sistema', models.AutoField(primary_key=True, serialize=False)),
                ('ativo', models.BooleanField(default=True, verbose_name='Status')),
                ('sistema', models.CharField(max_length=128, verbose_name='Aplicação')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição do Serviço')),
                ('fk_Cadeia_Servico', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Cadeia_Servico', verbose_name='Cadeia de Serviço')),
                ('fk_Responsavel_Dev', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Responsavel_Desenvolvimento', verbose_name='Desenvolvimento')),
                ('fk_Responsavel_Sup', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Responsavel_Suporte', verbose_name='Suporte')),
            ],
            options={
                'verbose_name': 'Sistema',
                'verbose_name_plural': 'Sistemas',
            },
        ),
        migrations.CreateModel(
            name='t_Infraestrutura',
            fields=[
                ('cod_Infraestrutura', models.AutoField(primary_key=True, serialize=False)),
                ('camada_balanceador', models.CharField(max_length=255, verbose_name='Estrutura da Camada do Balanceador')),
                ('camada_aplicacao', models.CharField(max_length=255, verbose_name='Estrutura da Camada da Aplicação')),
                ('camada_banco_dados', models.CharField(max_length=255, verbose_name='Estrutura da Camada do Banco de Dados')),
                ('fk_Sistema', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Sistema', verbose_name='Aplicação')),
                ('impacto_Direto', models.ManyToManyField(blank=True, to='systems.t_Impacto_Direto', verbose_name='Impacto Direto')),
                ('impacto_Indireto', models.ManyToManyField(blank=True, to='systems.t_Impacto_Indireto', verbose_name='Impacto Indireto')),
            ],
            options={
                'verbose_name': 'Infraestrutura Sistêmica',
                'verbose_name_plural': 'Infraestrutura Sistêmica',
            },
        ),
        migrations.CreateModel(
            name='t_Impacto_Negocio',
            fields=[
                ('cod_Impacto', models.AutoField(primary_key=True, serialize=False)),
                ('cliente', models.CharField(choices=[('', ''), ('Int', 'Internos'), ('Ext', 'Externos'), ('Ambos', 'Ambos')], default='', max_length=5, verbose_name='Impacta clientes:')),
                ('perda_Receita', models.CharField(choices=[('', ''), ('D', 'Direto'), ('I', 'Indireto'), ('N/A', 'Sem Impacto')], default='', max_length=3, verbose_name='Gera perda de receita?')),
                ('despesas_Adicionais', models.CharField(choices=[('', ''), ('D', 'Direto'), ('I', 'Indireto'), ('N/A', 'Sem Impacto')], default='', max_length=3, verbose_name='Gera despesas adicionais?')),
                ('elevacao_Custo_Transacional', models.CharField(choices=[('', ''), ('D', 'Direto'), ('I', 'Indireto'), ('N/A', 'Sem Impacto')], default='', max_length=3, verbose_name='Gera elevação do custo transacional?')),
                ('afeta_Disponibilidade', models.CharField(choices=[('', ''), ('D', 'Direto'), ('I', 'Indireto'), ('N/A', 'Sem Impacto')], default='', max_length=3, verbose_name='Afeta a disponibilidade?')),
                ('afeta_Imagem_IF', models.CharField(choices=[('', ''), ('D', 'Direto'), ('I', 'Indireto'), ('N/A', 'Sem Impacto')], default='', max_length=3, verbose_name='Afeta a imagem da TecBan com as IFs?')),
                ('afeta_Imagem_Consumidor', models.CharField(choices=[('', ''), ('D', 'Direto'), ('I', 'Indireto'), ('N/A', 'Sem Impacto')], default='', max_length=3, verbose_name='Afeta a imagem da TecBan com o Consumidor Final?')),
                ('impacto_Operacional', models.CharField(choices=[('', ''), ('D', 'Direto'), ('I', 'Indireto'), ('N/A', 'Sem Impacto')], default='', max_length=3, verbose_name='Gera impacto operacional?')),
                ('impacto_Adm', models.CharField(choices=[('', ''), ('D', 'Direto'), ('I', 'Indireto'), ('N/A', 'Sem Impacto')], default='', max_length=3, verbose_name='Gera impacto administrativo?')),
                ('impacto_Contratual', models.CharField(choices=[('', ''), ('D', 'Direto'), ('I', 'Indireto'), ('N/A', 'Sem Impacto')], default='', max_length=3, verbose_name='Gera impacto contratual?')),
                ('impacto_Legal', models.CharField(choices=[('', ''), ('D', 'Direto'), ('I', 'Indireto'), ('N/A', 'Sem Impacto')], default='', max_length=3, verbose_name='Gera impacto legal?')),
                ('RTO_Usuario', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Limite de Reestabelecimento Proposto')),
                ('criticidade', models.CharField(choices=[('', ''), ('Não Aplicável', 'Não Aplicável'), ('Não Crítico', 'Não Crítico'), ('Importante', 'Importante'), ('Crítico', 'Crítico'), ('Missão Crítica', 'Missão Crítica'), ('Infraestrutura', 'Infraestrutura')], default='', max_length=14, verbose_name='Criticidade da Aplicação')),
                ('observacoes', models.TextField(blank=True, verbose_name='Observações')),
                ('fk_Sistema', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Sistema', verbose_name='Aplicação')),
                ('fk_Usuario', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Usuario_Chave', verbose_name='Usuário Chave')),
                ('impactos_Potenciais', models.ManyToManyField(to='systems.t_Impacto_Potencial', verbose_name='Impactos Potenciais')),
                ('janelas_Criticas', models.ManyToManyField(to='systems.t_Sistema_Janelas', verbose_name='Janelas Críticas')),
            ],
            options={
                'verbose_name': 'Impacto de Negócio',
                'verbose_name_plural': 'Impactos de Negócio',
            },
        ),
        migrations.CreateModel(
            name='t_Criticidade',
            fields=[
                ('cod_Criticidade', models.AutoField(primary_key=True, serialize=False)),
                ('nivel_Criticidade', models.CharField(choices=[('', ''), ('AC', 'AC'), ('ACN', 'ACN'), ('ACN+', 'ACN+')], default='', max_length=4, verbose_name='Nível de Criticidade')),
                ('RTO', models.DecimalField(blank=True, decimal_places=2, max_digits=4, verbose_name='RTO')),
                ('fk_Sistema', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Sistema', verbose_name='Aplicação')),
            ],
            options={
                'verbose_name': 'Nível de Criticidade',
                'verbose_name_plural': 'Nível de Criticidade',
            },
        ),
        migrations.CreateModel(
            name='t_Continuidade_Tecnologica',
            fields=[
                ('cod_Continuidade', models.AutoField(primary_key=True, serialize=False)),
                ('camada_balanceador', models.CharField(choices=[('Disponibilidade', (('', ''), ('Alta Disp. Local', 'Alta Disp. Local'), ('Alta Disp. Entre Sites', 'Alta Disp. Entre Sites'), ('Infraestrutura Segmentada Por Raias', 'Infraestrutura Segmentada Por Raias'), ('N/A', 'N/A'))), ('Contingência', (('', ''), ('Contingência Local Manual', 'Contingência Local Manual'), ('Contingência Local Automática', 'Contingência Lcal Automática'), ('Contingência Entre Sites Manual', 'Contingência Entre Sites Manual'), ('Contingência Entre Sites Automática', 'Contingência Entre Sites Automática'), ('N/A', 'N/A')))], default='', max_length=35, verbose_name='Camada do Balanceador')),
                ('camada_aplicacao', models.CharField(choices=[('Disponibilidade', (('', ''), ('Alta Disp. Local', 'Alta Disp. Local'), ('Alta Disp. Entre Sites', 'Alta Disp. Entre Sites'), ('Infraestrutura Segmentada Por Raias', 'Infraestrutura Segmentada Por Raias'), ('N/A', 'N/A'))), ('Contingência', (('', ''), ('Contingência Local Manual', 'Contingência Local Manual'), ('Contingência Local Automática', 'Contingência Lcal Automática'), ('Contingência Entre Sites Manual', 'Contingência Entre Sites Manual'), ('Contingência Entre Sites Automática', 'Contingência Entre Sites Automática'), ('N/A', 'N/A')))], default='', max_length=35, verbose_name='Camada da Aplicação')),
                ('camada_banco_dados', models.CharField(choices=[('Disponibilidade', (('', ''), ('Alta Disp. Local', 'Alta Disp. Local'), ('Alta Disp. Entre Sites', 'Alta Disp. Entre Sites'), ('Infraestrutura Segmentada Por Raias', 'Infraestrutura Segmentada Por Raias'), ('N/A', 'N/A'))), ('Contingência', (('', ''), ('Contingência Local Manual', 'Contingência Local Manual'), ('Contingência Local Automática', 'Contingência Lcal Automática'), ('Contingência Entre Sites Manual', 'Contingência Entre Sites Manual'), ('Contingência Entre Sites Automática', 'Contingência Entre Sites Automática'), ('N/A', 'N/A')))], default='', max_length=35, verbose_name='Camada do Banco de Dados')),
                ('plano_De_Recup_Doc', models.CharField(choices=[('', ''), ('S', 'Sim'), ('N', 'Não'), ('C', 'À Confirmar')], default='', max_length=1, verbose_name='Possui plano de recuperação documentado?')),
                ('plano_De_Recup_Test', models.CharField(choices=[('', ''), ('S', 'Sim'), ('N', 'Não'), ('C', 'À Confirmar')], default='', max_length=1, verbose_name='Possui plano de recuperação testado?')),
                ('url_Ficheiro', models.URLField(blank=True, max_length=250, verbose_name='URL - Documentação')),
                ('fk_Sistema', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Sistema', verbose_name='Aplicação')),
            ],
            options={
                'verbose_name': 'Continuidade Tecnológica',
                'verbose_name_plural': 'Continuidade Tecnológica',
            },
        ),
        migrations.CreateModel(
            name='t_Contingencia',
            fields=[
                ('cod_Contingencia', models.AutoField(primary_key=True, serialize=False)),
                ('contingencia_Usuario', models.CharField(choices=[('', ''), ('Sim', 'Sim'), ('Não', 'Não'), ('À Confirmar', 'À Confirmar')], default='', max_length=11, verbose_name='Aplicação Contingenciada pelo Usuário?')),
                ('RTO_Contingencia', models.DecimalField(blank=True, decimal_places=2, max_digits=4, verbose_name='RTO Contingência')),
                ('fk_Impacto', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='systems.t_Impacto_Negocio', verbose_name='Contingência para:')),
                ('nome_Cont_User', models.ManyToManyField(blank=True, to='systems.t_Contingencia_Usuario', verbose_name='Tipo de Contigência')),
            ],
            options={
                'verbose_name': 'Contingência',
                'verbose_name_plural': 'Contingências',
            },
        ),
    ]
