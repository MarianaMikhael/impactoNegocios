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


class t_Responsavel_Desenvolvimento(models.Model):
    cod_Responsavel_Dev = models.AutoField(primary_key=True)
    area_Dev = models.CharField(max_length=128, blank=False,
                                verbose_name='Área de Desenvolvimento')
    nome_Resp_Area = models.CharField(max_length=128, blank=False,
                                     verbose_name='Responsável Pela Área')
    celula_Dev = models.CharField(max_length=128, blank=True,
                                  verbose_name='Célula de Desenvolvimento')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return '{}, {}'.format(self.area_Dev, self.celula_Dev)

    class Meta:
        verbose_name = 'Responsável pelo Desenvolvimento'
        verbose_name_plural = 'Responsáveis pelo Desenvolvimento'


class t_Responsavel_Suporte(models.Model):
    cod_Responsavel_Sup = models.AutoField(primary_key=True)
    area_Sup = models.CharField(max_length=128, blank=False,
                                verbose_name='Área de Suporte')
    nome_Resp_Area = models.CharField(max_length=128, blank=False,
                                     verbose_name='Responsável Pela Área')
    celula_Sup = models.CharField(max_length=128, blank=True,
                                  verbose_name='Célula de Suporte')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return '{}, {}'.format(self.area_Sup, self.celula_Sup)

    class Meta:
        verbose_name = 'Responsável pelo Suporte'
        verbose_name_plural = 'Responsáveis pelo Suporte'


class t_Sistema(models.Model):
    cod_Sistema = models.AutoField(primary_key=True)
    ativo = models.BooleanField(default=True,
                                verbose_name='Status')
    sistema = models.CharField(max_length=128,
                               blank=False,
                               verbose_name='Aplicação')
    descricao = models.TextField(blank=True,
                                 verbose_name='Descrição do Serviço')
    fk_Cadeia_Servico = models.ForeignKey(t_Cadeia_Servico,
                                          on_delete=models.PROTECT,
                                          default='',
                                          verbose_name='Cadeia de Serviço')
    fk_Responsavel_Dev = models.ForeignKey(t_Responsavel_Desenvolvimento,
                                           on_delete=models.PROTECT,
                                           default='',
                                           verbose_name='Desenvolvimento')
    fk_Responsavel_Sup = models.ForeignKey(t_Responsavel_Suporte,
                                           on_delete=models.PROTECT,
                                           default='',
                                           verbose_name='Suporte')  

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return self.sistema

    class Meta:
        verbose_name = 'Sistema'
        verbose_name_plural = 'Sistemas'


class t_Continuidade_Tecnologica(models.Model):
    cont_tec = [
        ('Disponibilidade', (
            ('', ''),
            ('Alta Disp. Local', 'Alta Disp. Local'),
            ('Alta Disp. Entre Sites', 'Alta Disp. Entre Sites'),
            ('Infraestrutura Segmentada Por Raias', 'Infraestrutura Segmentada Por Raias'),
            ('N/A', 'N/A'),
            )
        ),
        ('Contingência', (
            ('', ''),
            ('Contingência Local Manual', 'Contingência Local Manual'),
            ('Contingência Local Automática', 'Contingência Local Automática'),
            ('Contingência Entre Sites Manual', 'Contingência Entre Sites Manual'),
            ('Contingência Entre Sites Automática', 'Contingência Entre Sites Automática'),
            ('N/A', 'N/A'),
            )
        ),
    ]

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
                                   verbose_name='Aplicação')
    camada_balanceador = models.CharField(max_length=35,
                                          choices=cont_tec,
                                          default='',
                                          verbose_name='Camada do Balanceador')
    camada_aplicacao = models.CharField(max_length=35,
                                        choices=cont_tec,
                                        default='',
                                        verbose_name='Camada da Aplicação')
    camada_banco_dados = models.CharField(max_length=35,
                                          choices=cont_tec,
                                          default='',
                                          verbose_name='Camada do Banco de Dados')
    plano_De_Recup_Doc = models.CharField(max_length=1,
                                          choices=recup_choices,
                                          default='',
                                          verbose_name='Possui plano de recuperação documentado?')
    plano_De_Recup_Test = models.CharField(max_length=1,
                                           choices=recup_choices,
                                           default='',
                                           verbose_name='Possui plano de recuperação testado?')
    url_Ficheiro = models.URLField(max_length=500,
                                   blank=True,
                                   verbose_name='URL - Documentação')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return self.fk_Sistema.sistema

    class Meta:
        verbose_name = 'Continuidade Tecnológica'
        verbose_name_plural = 'Continuidade Tecnológica'


class t_Criticidade(models.Model):
    nivel_crit_choices = (
        ('', ''),
        ('AC', 'AC'),
        ('ACN', 'ACN'),
        ('ACN+', 'ACN+'),
    )

    cod_Criticidade = models.AutoField(primary_key=True)
    fk_Sistema = models.ForeignKey(t_Sistema,
                                   on_delete=models.PROTECT,
                                   default='',
                                   verbose_name='Aplicação')
    nivel_Criticidade = models.CharField(max_length=4,
                                         choices=nivel_crit_choices,
                                         default='',
                                         verbose_name='Nível de Criticidade')
    RTO = models.DecimalField(max_digits=4, decimal_places=2,
                              blank=True,
                              verbose_name='RTO')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return self.fk_Sistema.sistema

    class Meta:
        verbose_name = 'Nível de Criticidade'
        verbose_name_plural = 'Nível de Criticidade'


class t_Impacto_Direto(models.Model):
    cod_Imp_Direto = models.AutoField(primary_key=True)
    impacto_Direto = models.CharField(max_length=255,
                                 blank=True,
                                 verbose_name='Serviço Impactado Diretamente')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return self.impacto_Direto

    class Meta:
        verbose_name = 'Impacto Direto'
        verbose_name_plural = 'Impactos Diretos'


class t_Impacto_Indireto(models.Model):
    cod_Imp_Indireto = models.AutoField(primary_key=True)
    impacto_Indireto = models.CharField(max_length=255,
                                   blank=True,
                                   verbose_name='Serviço Impactado Indiretamente')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return self.impacto_Indireto

    class Meta:
        verbose_name = 'Impacto Indireto'
        verbose_name_plural = 'Impactos Indiretos'


class t_Infraestrutura(models.Model):
    cod_Infraestrutura =  models.AutoField(primary_key=True)
    fk_Sistema = models.ForeignKey(t_Sistema,
                                   on_delete=models.PROTECT,
                                   default='',
                                   verbose_name='Aplicação')
    camada_balanceador = models.CharField(max_length=255,
                                          blank=False,
                                          verbose_name='Estrutura da Camada do Balanceador')
    camada_aplicacao = models.CharField(max_length=255,
                                        blank=False,
                                        verbose_name='Estrutura da Camada da Aplicação')
    camada_banco_dados = models.CharField(max_length=255,
                                          blank=False,
                                          verbose_name='Estrutura da Camada do Banco de Dados')
    impacto_Direto = models.ManyToManyField(t_Impacto_Direto, blank=True,
                                            verbose_name="Impacto Direto")
    impacto_Indireto = models.ManyToManyField(t_Impacto_Indireto, blank=True,
                                              verbose_name="Impacto Indireto")
    # topologia = models.ImageField(upload_to='')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return self.fk_Sistema.sistema

    class Meta:
        verbose_name = 'Infraestrutura Sistêmica'
        verbose_name_plural = 'Infraestrutura Sistêmica'


class t_Usuario_Chave(models.Model):
    cod_Usuario_Chave = models.AutoField(primary_key=True)
    area_Usuario = models.CharField(max_length=128, blank=False,
                                    verbose_name='Área do Usuário')
    usuario_Chave = models.CharField(max_length=128,
                                     blank=False,
                                     verbose_name='Usuário Chave')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return '{} - {}'.format(self.area_Usuario, self.usuario_Chave)

    class Meta:
        verbose_name = 'Usuário Chave'
        verbose_name_plural = 'Usuários Chave'


class t_Impacto_Potencial(models.Model):
    cod_Impacto_Potencial = models.AutoField(primary_key=True)
    impacto_Potencial = models.CharField(max_length=255,
                                         blank=False,
                                         verbose_name='Consequência Causada Por Indisponibilidade Sistêmica')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return self.impacto_Potencial

    class Meta:
        verbose_name = 'Impacto Potencial'
        verbose_name_plural = 'Impactos Potenciais'


class t_Sistema_Janelas(models.Model):
    cod_Janela = models.AutoField(primary_key=True)
    janela_Critica = models.CharField(max_length=128,
                                      blank=False,
                                      verbose_name='Período')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return self.janela_Critica

    class Meta:
        verbose_name = 'Janela Crítica'
        verbose_name_plural = 'Janelas Críticas'
        

class t_Impacto_Negocio(models.Model):
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

    crit_sup_choices = (
        ('', ''),
        ('Não Aplicável', 'Não Aplicável'),
        ('Não Crítico', 'Não Crítico'),
        ('Importante', 'Importante'),
        ('Crítico', 'Crítico'),
        ('Missão Crítica', 'Missão Crítica'),
        ('Infraestrutura', 'Infraestrutura'),
    )

    cod_Impacto = models.AutoField(primary_key=True)
    fk_Usuario = models.ForeignKey(t_Usuario_Chave,
                                   on_delete=models.PROTECT,
                                   default='',
                                   verbose_name='Usuário Chave')
    fk_Sistema = models.ForeignKey(t_Sistema,
                                   on_delete=models.PROTECT,
                                   default='',
                                   verbose_name='Aplicação')
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
                                       verbose_name='Afeta a imagem da TecBan com as IFs?')
    afeta_Imagem_Consumidor = models.CharField(max_length=3,
                                               choices=impacto_choices,
                                               default='',
                                               verbose_name='Afeta a imagem da TecBan com o Consumidor Final?')
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
                                          verbose_name='Gera impacto contratual?')
    impacto_Legal = models.CharField(max_length=3,
                                     choices=impacto_choices,
                                     default='',
                                     verbose_name='Gera impacto legal?')
    impactos_Potenciais = models.ManyToManyField(t_Impacto_Potencial, blank=False,
                                                 verbose_name="Impactos Potenciais")
    janelas_Criticas = models.ManyToManyField(t_Sistema_Janelas, blank=False,
                                              verbose_name="Janelas Críticas")
    RTO_Usuario = models.DecimalField(max_digits=4, decimal_places=2,
                                       blank=False,
                                       verbose_name='Limite de Reestabelecimento Proposto')
    criticidade = models.CharField(max_length=14,
                                   choices=crit_sup_choices,
                                   default='',
                                   verbose_name='Criticidade da Aplicação')
    observacoes = models.TextField(blank=True,
                                   verbose_name='Observações')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return '{} - {}'.format(self.fk_Sistema.sistema, self.fk_Usuario.usuario_Chave)

    class Meta:
        verbose_name = 'Impacto de Negócio'
        verbose_name_plural = 'Impactos de Negócio'
    

class t_Contingencia_Usuario(models.Model):
    cod_Nome = models.AutoField(primary_key=True)
    nome_Contingencia = models.CharField(max_length=128,
                                         verbose_name='Nome da Contingência')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return self.nome_Contingencia

    class Meta:
        verbose_name = 'Contingência do Usuário'
        verbose_name_plural = 'Contingências do Usuário'


class t_Contingencia(models.Model):
    conting_choices = (
        ('', ''),
        ('Sim', 'Sim'),
        ('Não', 'Não'),
        ('À Confirmar', 'À Confirmar')
    )

    cod_Contingencia = models.AutoField(primary_key=True)
    fk_Impacto = models.ForeignKey(t_Impacto_Negocio,
                                   on_delete=models.PROTECT,
                                   default='',
                                   verbose_name='Contingência para:')
    contingencia_Usuario = models.CharField(max_length=11,
                                            choices=conting_choices,
                                            default='',
                                            verbose_name='Aplicação Contingenciada pelo Usuário?')
    nome_Cont_User = models.ManyToManyField(t_Contingencia_Usuario, blank=True,
                                              verbose_name="Tipo de Contigência")                                           
    RTO_Contingencia = models.DecimalField(max_digits=4, decimal_places=2,
                                           null = True, blank=True,
                                           verbose_name='RTO Contingência')

    # nomeia o objeto conforme o atributo escolhido
    def __str__(self):
        return str(self.fk_Impacto)

    class Meta:
        verbose_name = 'Contingência'
        verbose_name_plural = 'Contingências'
