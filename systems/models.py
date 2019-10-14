from django.db import models


# Create your models here.


class t_Cadeia_Servico(models.Model):
    cod_Cadeia_Servico = models.AutoField(primary_key=True)
    cadeia_Servico = models.CharField(max_length=128,
                                      blank=False,
                                      verbose_name='Nome')
    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return self.cadeia_Servico

    class Meta:
        verbose_name = 'Cadeia de Serviço'
        verbose_name_plural = 'Cadeia de Serviço'


class t_Area_Desenvolvimento(models.Model):
    cod_Area_Dev = models.AutoField(primary_key=True)
    area_Dev = models.CharField(max_length=128,
                                blank=False,
                                verbose_name='Área')
    gerente_Area_Dev = models.CharField(max_length=128, blank=True,
                                        verbose_name='Gerente')
    coordenador_Area_Dev = models.CharField(max_length=128, blank=True,
                                            verbose_name='Coordenador')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return self.area_Dev

    class Meta:
        verbose_name = 'Área de Desenvolvimento'
        verbose_name_plural = 'Áreas de Desenvolvimento'


class t_Area_Suporte(models.Model):
    cod_Area_Sup = models.AutoField(primary_key=True)
    area_Sup = models.CharField(max_length=128,
                                blank=False,
                                verbose_name='Área')
    gerente_Area_Sup = models.CharField(max_length=128, blank=True,
                                        verbose_name='Gerente')
    coordenador_Area_Sup = models.CharField(max_length=128, blank=True,
                                            verbose_name='Coordenador')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return self.area_Sup

    class Meta:
        verbose_name = 'Área de Suporte'
        verbose_name_plural = 'Áreas de Suporte'


class t_Responsavel_Desenvolvimento(models.Model):
    cod_Responsavel_Dev = models.AutoField(primary_key=True)
    fk_Area_Dev = models.ForeignKey(t_Area_Desenvolvimento,
                                     on_delete=models.PROTECT,
                                     default='',
                                     verbose_name='Área')
    celula_Dev = models.CharField(max_length=128, blank=True,
                                  verbose_name='Célula de Desenvolvimento')
    nome_Resp_Dev = models.CharField(max_length=128, blank=True,
                                     verbose_name='Desenvolvedor Responsável')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return '{} ({}). {}'.format(self.celula_Dev, self.fk_Area_Dev, self.nome_Resp_Dev)

    class Meta:
        verbose_name = 'Responsável pelo Desenvolvimento'
        verbose_name_plural = 'Responsáveis pelo Desenvolvimento'


class t_Responsavel_Suporte(models.Model):
    cod_Responsavel_Sup = models.AutoField(primary_key=True)
    fk_Area_Sup = models.ForeignKey(t_Area_Suporte,
                                     on_delete=models.PROTECT,
                                     default='',
                                     verbose_name='Área')
    celula_Sup = models.CharField(max_length=128, blank=True,
                                  verbose_name='Célula de Sustentação')
    nome_Resp_Sup = models.CharField(max_length=128, blank=True,
                                     verbose_name='Sustentador Responsável')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return '{} ({}). {}'.format(self.celula_Sup, self.fk_Area_Sup, self.nome_Resp_Sup)

    class Meta:
        verbose_name = 'Responsável pelo Suporte'
        verbose_name_plural = 'Responsáveis pelo Suporte'


class t_Criticidade(models.Model):
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

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return '{} ({})'.format(self.criticidade_Suporte, self.nivel_Criticidade) 

    class Meta:
        verbose_name = 'Nível de Criticidade'
        verbose_name_plural = 'Nível de Criticidade'


class t_Sistema_Servico(models.Model):
    cod_Servico = models.AutoField(primary_key=True)
    servico = models.CharField(max_length=255,
                               blank=True,
                               verbose_name='Descrição')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return self.servico

    class Meta:
        verbose_name = 'Sistema (Serviço)'
        verbose_name_plural = 'Sistemas (Serviços)'


class t_Sistema_Janelas(models.Model):
    cod_Janela = models.AutoField(primary_key=True)
    janela_Critica = models.CharField(max_length=128,
                                      blank=False,
                                      verbose_name='Período')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return self.janela_Critica

    class Meta:
        verbose_name = 'Sistema (Janela Crítica)'
        verbose_name_plural = 'Sistemas (Janelas Críticas)'


class t_Sistema(models.Model):
    cod_Sistema = models.AutoField(primary_key=True)
    fk_Cadeia_Servico = models.ForeignKey(t_Cadeia_Servico,
                                           on_delete=models.PROTECT,
                                           default='',
                                           verbose_name='Cadeia de Serviço')
    fk_Responsavel_Dev = models.ForeignKey(t_Responsavel_Desenvolvimento,
                                            on_delete=models.PROTECT,
                                            default='',
                                            verbose_name='Célula de Desenvolvimento')
    fk_Responsavel_Sup = models.ForeignKey(t_Responsavel_Suporte,
                                            on_delete=models.PROTECT,
                                            default='',
                                            verbose_name='Célula de Sustentação')
    fk_Criticidade = models.ForeignKey(t_Criticidade,
                                        on_delete=models.PROTECT,
                                        default='',
                                        verbose_name='Criticidade')
    sistema = models.CharField(max_length=128,
                               blank=False,
                               verbose_name='Sistema')
    servicos = models.ManyToManyField(t_Sistema_Servico, blank=False,
                                      verbose_name="Serviço")
    janelas_Criticas = models.ManyToManyField(t_Sistema_Janelas, blank=False,
                                              verbose_name="Janelas Críticas")
    RTO_hrs = models.DecimalField(max_digits=4, decimal_places=2,
                                  blank=True,
                                  verbose_name='RTO(hrs)')
    servidores = models.CharField(max_length=128,
                                  blank=True,
                                  verbose_name='Servidores')
    url_Topologia = models.URLField(max_length=250,
                                blank=True,
                                verbose_name='URL - Topologia')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return self.sistema

    class Meta:
        verbose_name = 'Sistema'
        verbose_name_plural = 'Sistemas'


class t_Contingencia(models.Model):
    conting_choices = (
        ('', ''),
        ('S', 'Sim'),
        ('N', 'Não'),
        ('C', 'À Confirmar')
    )

    cod_Contingencia = models.AutoField(primary_key=True)
    fk_Sistema = models.ForeignKey(t_Sistema,
                                    on_delete=models.PROTECT,
                                    default='',
                                    verbose_name='Sistema')
    contingencia_Arquitetura = models.CharField(max_length=1,
                                                choices=conting_choices,
                                                default='',
                                                verbose_name='Contingenciado pela Arquitetura TecBan?')
    contingencia_Usuario = models.CharField(max_length=1,
                                            choices=conting_choices,
                                            default='',
                                            verbose_name='Contingenciado pelo Usuário?')
    RTO_Contingencia = models.DecimalField(max_digits=4, decimal_places=2,
                                           blank=True,
                                           verbose_name='RTO(hrs) Contingência')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return self.cod_Sistema

    class Meta:
        verbose_name = 'Contingência'
        verbose_name_plural = 'Contingências'


class t_Contingencia_Arquitetura(models.Model):
    cod_Nome = models.AutoField(primary_key=True)
    fk_Contingencia = models.ForeignKey(t_Contingencia,
                                         on_delete=models.PROTECT,
                                         default='',
                                         verbose_name='Sistema Contingenciado')
    nome_Contingencia = models.CharField(max_length=128,
                                         verbose_name='Nome da Contingência (Arquitetura)')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return self.nome_Contingencia

    class Meta:
        verbose_name = 'Contingência (Arquitetura TecBan)'
        verbose_name_plural = 'Contingências (Arquitetura TecBan)'


class t_Contingencia_Usuario(models.Model):
    cod_Nome = models.AutoField(primary_key=True)
    fk_Contingencia = models.ForeignKey(t_Contingencia,
                                         on_delete=models.PROTECT,
                                         default='',
                                         verbose_name='Sistema Contingenciado')
    nome_Contingencia = models.CharField(max_length=128,
                                         verbose_name='Nome da Contingência (Usuário)')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return self.nome_Contingencia

    class Meta:
        verbose_name = 'Contingência (Usuário)'
        verbose_name_plural = 'Contingências (Usuário)'


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
    fk_Sistema = models.ForeignKey(t_Sistema,
                                    on_delete=models.PROTECT,
                                    default='',
                                    verbose_name='Sistema')

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

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return self.continuidade_Tecnologica

    class Meta:
        verbose_name = 'Continuidade Tecnológica'
        verbose_name_plural = 'Continuidade Tecnológica'


class t_Continuidade_Tecnologica_Sites(models.Model):
    site_choices = (
        ('', ''),
        ('V', 'Vivo'),
        ('D', 'Diveo'),
        ('C', 'Cetem'),
    )

    cod_Continuidade_Tecnologica = models.AutoField(primary_key=True)
    fk_Continuidade = models.ForeignKey(t_Continuidade_Tecnologica,
                                         on_delete=models.PROTECT,
                                         default='',
                                         verbose_name='Continuidade Tecnológica')
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

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return self.site

    class Meta:
        verbose_name = 'Continuidade Tecnológica (Site)'
        verbose_name_plural = 'Continuidade Tecnológica (Sites)'


class t_Impacto_Fronteira(models.Model):
    cod_Fronteira = models.AutoField(primary_key=True)
    fronteira = models.CharField(max_length=128,
                                 blank=True,
                                 verbose_name='Nome da Aplicação Que Faz Fronteira')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return self.fronteira

    class Meta:
        verbose_name = 'Impacto (Fronteira)'
        verbose_name_plural = 'Impactos (Fronteiras)'


class t_Impacto_Dependencia(models.Model):
    cod_Dependencia = models.AutoField(primary_key=True)
    dependencia = models.CharField(max_length=128,
                                   blank=True,
                                   verbose_name='Nome da Aplicação Dependente')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return self.dependencia

    class Meta:
        verbose_name = 'Impacto (Dependência)'
        verbose_name_plural = 'Impactos (Dependências)'


class t_Impacto_Usuario(models.Model):
    cod_Usuario_Chave = models.AutoField(primary_key=True)
    usuario_Chave = models.CharField(max_length=128,
                                     blank=False,
                                     verbose_name='Usuário Chave')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return self.usuario_Chave

    class Meta:
        verbose_name = 'Impacto (Usuário Chave)'
        verbose_name_plural = 'Impactos (Usuários Chave)'


class t_Impacto_Potencial(models.Model):
    cod_Impacto_Potencial = models.AutoField(primary_key=True)
    impacto_Potencial = models.CharField(max_length=255,
                                                   blank=False,
                                                   verbose_name='Consequência Causada Por Indisponibilidade')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return self.impacto_Potencial

    class Meta:
        verbose_name = 'Impacto Potencial'
        verbose_name_plural = 'Impactos Potenciais'


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
    fk_Sistema = models.ForeignKey(t_Sistema,
                                    on_delete=models.PROTECT,
                                    default='',
                                    verbose_name='Sistema')
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
    fronteiras = models.ManyToManyField(t_Impacto_Fronteira, blank=False,
                                        verbose_name="Fronteiras")
    dependencias = models.ManyToManyField(t_Impacto_Dependencia, blank=False,
                                          verbose_name="Dependências")
    usuario_Chave = models.ManyToManyField(t_Impacto_Usuario, blank=False,
                                           verbose_name="Usuários Chave")
    impactos_Potenciais = models.ManyToManyField(t_Impacto_Potencial, blank=False,
                                                 verbose_name="Impactos Potenciais")
    observacoes = models.TextField(blank=True,
                                   verbose_name='Observações')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return self.cliente

    class Meta:
        verbose_name = 'Impacto'
        verbose_name_plural = 'Impactos'
