from django.contrib import admin

# Register your models here.

from systems import models as m


class DevAdmin(admin.ModelAdmin):
    fields = ('nome_Resp_Area', ('area_Dev', 'celula_Dev'))
    list_display = ('celula_Dev', 'area_Dev', 'nome_Resp_Area')



class SupAdmin(admin.ModelAdmin):
    fields = ('nome_Resp_Area', ('area_Sup', 'celula_Sup'))
    list_display = ('celula_Sup', 'area_Sup', 'nome_Resp_Area')


class SistemaAdmin(admin.ModelAdmin):
    fields = ('ativo', ('fk_Cadeia_Servico', 'sistema'),
        ('fk_Responsavel_Dev', 'fk_Responsavel_Sup'), 'descricao')
    list_display = ('sistema', 'ativo')


class InfraAdmin(admin.ModelAdmin):
    fields = ('fk_Sistema', 'camada_balanceador', 'camada_aplicacao',
        'camada_banco_dados', ('impacto_Direto', 'impacto_Indireto'))


class ContAdmin(admin.ModelAdmin):
    fields = ('fk_Sistema', ('disp_balanceador', 'conting_balanceador'),
        ('disp_aplicacao', 'conting_aplicacao'), ('disp_banco_dados',
        'conting_banco_dados'), ('plano_De_Recup_Doc', 'plano_De_Recup_Test'),
        'url_Ficheiro')
    list_display = ('fk_Sistema', 'plano_De_Recup_Doc', 'url_Ficheiro')


class CriticAdmin(admin.ModelAdmin):
    fields = ('fk_Sistema', 'nivel_Criticidade', 'RTO')


class UserAdmin(admin.ModelAdmin):
    fields = ('area_Usuario', 'usuario_Chave')


class ImpAdmin(admin.ModelAdmin):
    fields = ('fk_Sistema', 'fk_Usuario', ('cliente', 'afeta_Disponibilidade',
        'impacto_Operacional'), ('perda_Receita', 'elevacao_Custo_Transacional',
        'despesas_Adicionais'), ('impacto_Adm', 'impacto_Contratual',
        'impacto_Legal'), ('afeta_Imagem_IF', 'afeta_Imagem_Consumidor'),
        ('RTO_Usuario', 'criticidade'), 'observacoes')


class ContingAdmin(admin.ModelAdmin):
    fields = ('fk_Sistema', 'fk_Impacto', ('contingencia_Usuario',
        'RTO_Contingencia'))


admin.site.register(m.t_Cadeia_Servico)
admin.site.register(m.t_Responsavel_Desenvolvimento, DevAdmin)
admin.site.register(m.t_Responsavel_Suporte, SupAdmin)
admin.site.register(m.t_Sistema, SistemaAdmin)
admin.site.register(m.t_Impacto_Direto)
admin.site.register(m.t_Impacto_Indireto)
admin.site.register(m.t_Infraestrutura, InfraAdmin)
admin.site.register(m.t_Continuidade_Tecnologica, ContAdmin)
admin.site.register(m.t_Criticidade, CriticAdmin)
admin.site.register(m.t_Usuario_Chave, UserAdmin)
admin.site.register(m.t_Impacto_Potencial)
admin.site.register(m.t_Sistema_Janelas)
admin.site.register(m.t_Impacto_Negocio, ImpAdmin)
admin.site.register(m.t_Contingencia_Usuario)
admin.site.register(m.t_Contingencia, ContingAdmin)
