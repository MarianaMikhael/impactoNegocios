from django.contrib import admin

# Register your models here.

from systems import models as m


admin.site.register(m.t_Cadeia_Servico),
admin.site.register(m.t_Area_Desenvolvimento),
admin.site.register(m.t_Area_Suporte),
admin.site.register(m.t_Responsavel_Desenvolvimento),
admin.site.register(m.t_Responsavel_Suporte),
admin.site.register(m.t_Criticidade),
admin.site.register(m.t_Sistema_Servico),
admin.site.register(m.t_Sistema_Janelas),
admin.site.register(m.t_Sistema),
admin.site.register(m.t_Contingencia),
admin.site.register(m.t_Contingencia_Arquitetura),
admin.site.register(m.t_Contingencia_Usuario),
admin.site.register(m.t_Continuidade_Tecnologica),
admin.site.register(m.t_Continuidade_Tecnologica_Sites),
admin.site.register(m.t_Impacto_Fronteira),
admin.site.register(m.t_Impacto_Dependencia),
admin.site.register(m.t_Impacto_Usuario),
admin.site.register(m.t_Impacto_Potencial),
admin.site.register(m.t_Impacto)

