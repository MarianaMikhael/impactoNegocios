from django.db import models


# Create your models here.


class t_Cadeia_Servico(models.Model):
    cod_Cadeia_Servico = models.AutoField(primary_key=True)
    cadeia_Servico = models.CharField(max_length=128,
                                      blank=False,
                                      verbose_name='Cadeia de Serviço')

    class Meta:
        verbose_name = 'Cadeia de Serviço'
        verbose_name_plural = 'Cadeia de Serviço'

        # nomeia o objeto conforme o atributo escolhido
        def __str__(self):
            return self.cadeia_Servico


class t_Area_Desenvolvimento(models.Model):
    cod_Area_Dev = models.AutoField(primary_key=True)
    area_Dev = models.CharField(max_length=128,
                                blank=False,
                                verbose_name='Área de Desenvolvimento')
    gerente_Area_Dev = models.CharField(max_length=128, blank=True,
                                        verbose_name='Gerente da Área de Desenvolvimento')
    coordenador_Area_Dev = models.CharField(max_length=128, blank=True,
                                            verbose_name='Coordenador da Área de Desenvolvimento')

    class Meta:
        verbose_name = 'Área de Desenvolvimento'
        verbose_name_plural = 'Área de Desenvolvimento'

        # nomeia o objeto conforme o atributo escolhido
        def __str__(self):
            return self.area_Dev


class t_Area_Suporte(models.Model):
    cod_Area_Sup = models.AutoField(primary_key=True)
    area_Sup = models.CharField(max_length=128,
                                blank=False,
                                verbose_name='Área de Suporte')
    gerente_Area_Sup = models.CharField(max_length=128, blank=True,
                                        verbose_name='Gerente da Área de Suporte')
    coordenador_Area_Sup = models.CharField(max_length=128, blank=True,
                                            verbose_name='Coordenador da Área de Suporte')

    class Meta:
        verbose_name = 'Área de Suporte'
        verbose_name_plural = 'Área de Suporte'

        # nomeia o objeto conforme o atributo escolhido
        def __str__(self):
            return self.area_Sup


class t_Responsavel_Desenvolvimento(models.Model):
    cod_Responsavel_Dev = models.AutoField(primary_key=True)
    cod_Area_Dev = models.ForeignKey(t_Area_Desenvolvimento,
                                     on_delete=models.CASCADE)
    nome_Resp_Dev = models.CharField(max_length=128, blank=True,
                                     verbose_name='Desenvolvedor Responsável')
    celula_Dev = models.CharField(max_length=128, blank=True,
                                  verbose_name='Célula de Desenvolvimento')

    class Meta:
        verbose_name = 'Responsável Desenvolvimento'
        verbose_name_plural = 'Responsável Desenvolvimento'

        # nomeia o objeto conforme o atributo escolhido
        def __str__(self):
            return self.nome_Resp_Dev


class t_Responsavel_Suporte(models.Model):
    cod_Responsavel_Sup = models.AutoField(primary_key=True)
    cod_Area_Sup = models.ForeignKey(t_Area_Suporte,
                                     on_delete=models.CASCADE)
    nome_Resp_Sup = models.CharField(max_length=128, blank=True,
                                     verbose_name='Sustentador Responsável')
    celula_Sup = models.CharField(max_length=128, blank=True,
                                  verbose_name='Célula de Sustentação')

    class Meta:
        verbose_name = 'Responsável Suporte'
        verbose_name_plural = 'Responsável Suporte'

        # nomeia o objeto conforme o atributo escolhido
        def __str__(self):
            return self.nome_Resp_Sup


class t_Criticidade_Suporte(models.Model):
    nivel_crit_choices = (
        ('', ''),
        ('AC', 'AC'),
        ('ACN', 'ACN'),
        ('ACN+', 'ACN+'),
    )

    crit_sup_choices = (
        ('', ''),
        ('Não Aplicável', 'Não Aplicável'),
        ('Não Crítico', 'Não Crítico'),
        ('Importante', 'Importante'),
        ('Crítico', 'Crítico'),
        ('Missão Crítica', 'Missão Crítica'),
        ('Infraestrutura', 'Infraestrutura'),
    )

    cod_Criticidade = models.AutoField(primary_key=True)
    nivel_Criticidade = models.CharField(max_length=4,
                                         choices=nivel_crit_choices,
                                         default='',
                                         verbose_name='Nível de Criticidade')
    criticidade_Suporte = models.CharField(max_length=14,
                                           choices=crit_sup_choices,
                                           default='',
                                           verbose_name='Criticidade Suporte')

    class Meta:
        verbose_name = 'Criticidade Suporte'
        verbose_name_plural = 'Criticidade Suporte'

        # nomeia o objeto conforme o atributo escolhido
        def __str__(self):
            return self.nivel_Criticidade


class t_Sistema(models.Model):
    cod_Sistema = models.AutoField(primary_key=True)
    cod_Cadeia_Servico = models.ForeignKey(t_Cadeia_Servico,
                                           on_delete=models.CASCADE)
    cod_Responsavel_Dev = models.ForeignKey(t_Responsavel_Desenvolvimento,
                                            on_delete=models.CASCADE)
    cod_Responsavel_Sup = models.ForeignKey(t_Responsavel_Suporte,
                                            on_delete=models.CASCADE)
    cod_Criticidade = models.ForeignKey(t_Criticidade_Suporte,
                                        on_delete=models.CASCADE)
    sistema = models.CharField(max_length=128,
                               blank=False,
                               verbose_name='Sistema')
    RTO_hrs = models.DecimalField(max_digits=4, decimal_places=2,
                                  blank=True,
                                  verbose_name='RTO(hrs)')
    servidores = models.CharField(max_length=128,
                                  blank=True,
                                  verbose_name='Servidores')
    topologia = models.URLField(max_length=250,
                                blank=True,
                                verbose_name='Topologia')

    class Meta:
        verbose_name = 'Sistema'
        verbose_name_plural = 'Sistemas'

        # nomeia o objeto conforme o atributo escolhido
        def __str__(self):
            return self.sistema


class t_Sistema_Servico(models.Model):
    cod_Servico = models.AutoField(primary_key=True)
    cod_Sistema = models.ForeignKey(t_Sistema,
                                    on_delete=models.CASCADE)
    servico = models.CharField(max_length=255,
                               blank=True,
                               verbose_name='Serviço')

    class Meta:
        verbose_name = 'Sistema - Serviço'
        verbose_name_plural = 'Sistema - Serviços'

        # nomeia o objeto conforme o atributo escolhido
        def __str__(self):
            return self.cod_Sistema


class t_Sistema_Janelas(models.Model):
    cod_Janela = models.AutoField(primary_key=True)
    cod_Sistema = models.ForeignKey(t_Sistema,
                                    on_delete=models.CASCADE)
    janela_Critica = models.CharField(max_length=128,
                                      blank=False,
                                      verbose_name='Janela Crítica')

    class Meta:
        verbose_name = 'Sistema - Janela Crítica'
        verbose_name_plural = 'Sistema - Janelas Críticas'

        # nomeia o objeto conforme o atributo escolhido
        def __str__(self):
            return self.cod_Sistema


class t_Contingencia(models.Model):
    conting_choices = (
        ('', ''),
        ('S', 'Sim'),
        ('N', 'Não'),
        ('C', 'À Confirmar')
    )

    cod_Contingencia = models.AutoField(primary_key=True)
    cod_Sistema = models.ForeignKey(t_Sistema,
                                    on_delete=models.CASCADE)
    contingencia_Arquitetura = models.CharField(max_length=1,
                                                choices=conting_choices,
                                                default='',
                                                verbose_name='Contingenciado pela Arquitetura TecBan?')
    contingencia_Usuario = models.CharField(max_length=1,
                                            choices=conting_choices,
                                            default='',
                                            verbose_name='Contingenciado pelo Usuário')
    RTO_Contingencia = models.DecimalField(max_digits=4, decimal_places=2,
                                           blank=True,
                                           verbose_name='RTO(hrs) Contingência ')

    class Meta:
        verbose_name = 'Contingência'
        verbose_name_plural = 'Contingências'

        # nomeia o objeto conforme o atributo escolhido
        def __str__(self):
            return self.cod_Sistema


class t_Contingencia_Arquitetura_Nome(models.Model):
    cod_Nome = models.AutoField(primary_key=True)
    cod_Contingencia = models.ForeignKey(t_Contingencia,
                                         on_delete=models.CASCADE)
    nome_Contingencia = models.CharField(max_length=128,
                                         verbose_name='Contingência Arquitetura')

    class Meta:
        verbose_name = 'Contingência Arquitetura - Nome'
        verbose_name_plural = 'Contingência Arquitetura - Nomes'

        # nomeia o objeto conforme o atributo escolhido
        def __str__(self):
            return self.cod_Contingencia


class t_Contingencia_Usuario_Nome(models.Model):
    cod_Nome = models.AutoField(primary_key=True)
    cod_Contingencia = models.ForeignKey(t_Contingencia,
                                         on_delete=models.CASCADE)
    nome_Contingencia = models.CharField(max_length=128,
                                         verbose_name='Contingência Usuário')

    class Meta:
        verbose_name = 'Contingência Usuário - Nome'
        verbose_name_plural = 'Contingência Usuário - Nomes'

        # nomeia o objeto conforme o atributo escolhido
        def __str__(self):
            return self.cod_Contingencia


class t_Continuidade_Tecnologica(models.Model):
    cont_tec_choices = (
        ('', ''),
        ('DR', 'Disaster Recovery'),
        ('AD', 'Alta Disponibilidade'),
    )

    recup_choices = (
        ('', ''),
        ('S', 'Sim'),
        ('N', 'Não'),
        ('C', 'À Confirmar'),
    )

    cod_Continuidade = models.AutoField(primary_key=True)
    cod_Sistema = models.ForeignKey(t_Sistema,
                                    on_delete=models.CASCADE)

    continuidade_Tecnologica = models.CharField(max_length=2,
                                                choices=cont_tec_choices,
                                                default='',
                                                verbose_name='Continuidade Tecnológica')
    plano_De_Recup_Doc = models.CharField(max_length=1,
                                          choices=recup_choices,
                                          default='',
                                          verbose_name='Possui plano de recuperação documentado?')
    plano_De_Recup_Test = models.CharField(max_length=1,
                                           choices=recup_choices,
                                           default='',
                                           verbose_name='Possui plano de recuperação testado?')
    url_Ficheiro = models.URLField(max_length=250,
                                   blank=True,
                                   verbose_name='URL - Documentação')

    class Meta:
        verbose_name = 'Continuidade Tecnológica'
        verbose_name_plural = 'Continuidade Tecnológica'

        # nomeia o objeto conforme o atributo escolhido
        def __str__(self):
            return self.cod_Sistema


class t_Continuidade_Tecnologica_Sites(models.Model):
    site_choices = (
        ('', ''),
        ('V', 'Vivo'),
        ('D', 'Diveo'),
        ('C', 'Cetem'),
    )

    cod_Continuidade_Tecnologica = models.AutoField(primary_key=True)
    cod_Continuidade = models.ForeignKey(t_Continuidade_Tecnologica,
                                         on_delete=models.CASCADE)
    camada = models.IntegerField(choices=list(zip(range(1, 16), range(1, 16))),
                                 verbose_name='Camada de Serviço')
    # models.IntegerField(choices=list(zip(range(1, 10), range(1, 10))))
    servico = models.CharField(max_length=128,
                               blank=False,
                               verbose_name='Serviço')
    site = models.CharField(max_length=1,
                            choices=site_choices,
                            default='',
                            verbose_name='Site (DataCenter)')
    observacao = models.TextField(blank=True,
                                  verbose_name='Observações')

    class Meta:
        verbose_name = 'Continuidade Tecnológica - Sites'
        verbose_name_plural = 'Continuidade Tecnológica - Sites'

        # nomeia o objeto conforme o atributo escolhido
        def __str__(self):
            return self.cod_Continuidade


class t_Impacto(models.Model):
    impacto_choices = (
        ('', ''),
        ('D', 'Direto'),
        ('I', 'Indireto'),
        ('N/A', 'Sem Impacto'),
    )

    cliente_choices = (
        ('', ''),
        ('Int', 'Internos'),
        ('Ext', 'Externos'),
        ('Ambos', 'Ambos'),
    )

    cod_Impacto = models.AutoField(primary_key=True)
    cod_Sistema = models.ForeignKey(t_Sistema,
                                    on_delete=models.CASCADE)
    cliente = models.CharField(max_length=5,
                               choices=cliente_choices,
                               default='',
                               verbose_name='Impacta clientes:')
    perda_Receita = models.CharField(max_length=3,
                                     choices=impacto_choices,
                                     default='',
                                     verbose_name='Gera perda de receita?')
    despesas_Adicionais = models.CharField(max_length=3,
                                           choices=impacto_choices,
                                           default='',
                                           verbose_name='Gera despesas adicionais?')
    elevacao_Custo_Transacional = models.CharField(max_length=3,
                                                   choices=impacto_choices,
                                                   default='',
                                                   verbose_name='Gera elevação do custo transacional?')
    afeta_Disponibilidade = models.CharField(max_length=3,
                                             choices=impacto_choices,
                                             default='',
                                             verbose_name='Afeta a disponibilidade?')
    afeta_Imagem_IF = models.CharField(max_length=3,
                                       choices=impacto_choices,
                                       default='',
                                       verbose_name='Afeta a imagem da Tecban com as IFs?')
    afeta_Imagem_Consumidor = models.CharField(max_length=3,
                                               choices=impacto_choices,
                                               default='',
                                               verbose_name='Afeta a imagem da TecBan com o consumidor final?')
    impacto_Operacional = models.CharField(max_length=3,
                                           choices=impacto_choices,
                                           default='',
                                           verbose_name='Gera impacto operacional?')
    impacto_Adm = models.CharField(max_length=3,
                                   choices=impacto_choices,
                                   default='',
                                   verbose_name='Gera impacto administrativo?')
    impacto_Contratual = models.CharField(max_length=3,
                                          choices=impacto_choices,
                                          default='',
                                          verbose_name='gera impacto contratual?')
    impacto_Legal = models.CharField(max_length=3,
                                     choices=impacto_choices,
                                     default='',
                                     verbose_name='Gera impacto legal?')
    observacoes = models.TextField(blank=True,
                                   verbose_name='Observações')

    class Meta:
        verbose_name = 'Impacto'
        verbose_name_plural = 'Impactos'

        # nomeia o objeto conforme o atributo escolhido
        def __str__(self):
            return self.cod_Sistema


class t_Impacto_Dependencias(models.Model):
    cod_Dependencia = models.AutoField(primary_key=True)
    cod_Impacto = models.ForeignKey(t_Impacto,
                                    on_delete=models.CASCADE)
    dependencia = models.CharField(max_length=128,
                                   blank=True,
                                   verbose_name='Dependência(s)')

    class Meta:
        verbose_name = 'Impacto - Dependência'
        verbose_name_plural = 'Impacto - Dependências'

        # nomeia o objeto conforme o atributo escolhido
        def __str__(self):
            return self.cod_Impacto


class t_Impacto_Fronteiras(models.Model):
    cod_Fronteira = models.AutoField(primary_key=True)
    cod_impacto = models.ForeignKey(t_Impacto,
                                    on_delete=models.CASCADE)
    fronteira = models.CharField(max_length=128,
                                 blank=True,
                                 verbose_name='Fronteira(s)')

    class Meta:
        verbose_name = 'Impacto - Fronteira'
        verbose_name_plural = 'Impacto - Fronteiras'

        # nomeia o objeto conforme o atributo escolhido
        def __str__(self):
            return self.cod_Impacto


class t_Impacto_Potenciais(models.Model):
    cod_Impacto_Potencial = models.AutoField(primary_key=True)
    cod_Impacto = models.ForeignKey(t_Impacto,
                                    on_delete=models.CASCADE)
    descricao_Impacto_Potencial = models.CharField(max_length=255,
                                                   blank=False,
                                                   verbose_name='Impacto(s) Potencial(is)')

    class Meta:
        verbose_name = 'Impacto Potencial'
        verbose_name_plural = 'Impactos Potenciais'

        # nomeia o objeto conforme o atributo escolhido
        def __str__(self):
            return self.cod_Impacto


class t_Impacto_Usuarios(models.Model):
    cod_Usuario_Chave = models.AutoField(primary_key=True)
    cod_Impacto = models.ForeignKey(t_Impacto,
                                    on_delete=models.CASCADE)
    usuario_Chave = models.CharField(max_length=128,
                                     blank=False,
                                     verbose_name='Usuário(s) Chave(s)')

    class Meta:
        verbose_name = 'Impacto - Usuário Chave'
        verbose_name_plural = 'Impacto - Usuários Chave'

        # nomeia o objeto conforme o atributo escolhido
        def __str__(self):
            return self.cod_Impacto
