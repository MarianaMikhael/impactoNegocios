from django.forms import ModelForm
from django import forms

import systems.models as m


class CadeiaServicoForm(ModelForm):
    class Meta:
        model = m.t_Cadeia_Servico
        fields = [
            'cadeia_Servico',
        ]


class ResponsavelDesenvolvimentoForm(ModelForm):
    class Meta:
        model = m.t_Responsavel_Desenvolvimento
        fields = [
            'area_Dev',
            'nome_Resp_Area',
            'celula_Dev',
        ]


class ResponsavelSuporteForm(ModelForm):
    class Meta:
        model = m.t_Responsavel_Suporte
        fields = [
            'area_Sup',
            'nome_Resp_Area',
            'celula_Sup',
        ]


class SistemaForm(ModelForm):
    class Meta:
        model = m.t_Sistema
        fields = [
            'ativo',
            'sistema',
            'descricao',
            'fk_Cadeia_Servico',
            'fk_Responsavel_Dev',
            'fk_Responsavel_Sup',
        ]


class ContinuidadeTecnologicaForm(ModelForm):
    class Meta:
        model = m.t_Continuidade_Tecnologica
        fields = [
            'fk_Sistema',
            'camada_balanceador',
            'camada_aplicacao',
            'camada_banco_dados',
            'plano_De_Recup_Doc',
            'plano_De_Recup_Test',
            'url_Ficheiro',
        ]


class CriticidadeForm(ModelForm):
    class Meta:
        model = m.t_Criticidade
        fields = [
            'fk_Sistema',
            'nivel_Criticidade',
            'RTO',
        ]


class ImpactoDiretoForm(ModelForm):
    class Meta:
        model = m.t_Impacto_Direto
        fields = [
            'impacto_Direto',
        ]


class ImpactoIndiretoForm(ModelForm):
    class Meta:
        model = m.t_Impacto_Indireto
        fields = [
            'impacto_Indireto',
        ]


class InfraestruturaForm(ModelForm):
    class Meta:
        model = m.t_Infraestrutura
        fields = [
            'fk_Sistema',
            'camada_balanceador',
            'camada_aplicacao',
            'camada_banco_dados',
            'impacto_Direto',
            'impacto_Indireto',
            # 'topologia',
        ]


class UsuarioChaveForm(ModelForm):
    class Meta:
        model = m.t_Usuario_Chave
        fields = [
            'area_Usuario',
            'usuario_Chave',
        ]


class ImpactoPotencialForm(ModelForm):
    class Meta:
        model = m.t_Impacto_Potencial
        fields = [
            'impacto_Potencial',
        ]


class SistemaJanelasForm(ModelForm):
    class Meta:
        model = m.t_Sistema_Janelas
        fields = [
            'janela_Critica',
        ]


class ImpactoNegocioForm(ModelForm):
    class Meta:
        model = m.t_Impacto_Negocio
        fields = [
            'fk_Usuario',
            'fk_Sistema',
            'cliente',
            'perda_Receita',
            'despesas_Adicionais',
            'elevacao_Custo_Transacional',
            'afeta_Disponibilidade',
            'afeta_Imagem_IF',
            'afeta_Imagem_Consumidor',
            'impacto_Operacional',
            'impacto_Adm',
            'impacto_Contratual',
            'impacto_Legal',
            'impactos_Potenciais',
            'janelas_Criticas',
            'RTO_Usuario',
            'criticidade',
            'observacoes',
        ]


class ContingenciaUsuarioForm(ModelForm):
    class Meta:
        model = m.t_Contingencia_Usuario
        fields = [
            'nome_Contingencia'
        ]


class ContingenciaForm(ModelForm):
    class Meta:
        model = m.t_Contingencia
        fields = [
            'fk_Impacto',
            'contingencia_Usuario',
            'nome_Cont_User',
            'RTO_Contingencia',
        ]
