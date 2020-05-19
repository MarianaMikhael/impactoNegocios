from django.forms import ModelForm
from django import forms

import systems.models as m


class CadeiaServicoForm(forms.ModelForm):
    class Meta:
        model = m.t_Cadeia_Servico
        exclude = ('cod_Cadeia_Servico', )


class ResponsavelDesenvolvimentoForm(forms.ModelForm):
    class Meta:
        model = m.t_Responsavel_Desenvolvimento
        exclude = ('cod_Responsavel_Dev', )


class ResponsavelSuporteForm(forms.ModelForm):
    class Meta:
        model = m.t_Responsavel_Suporte
        exclude = ('cod_Responsavel_Sup', )


class SistemaForm(forms.ModelForm):
    class Meta:
        model = m.t_Sistema
        exclude = ('cod_Sistema', )


class ImpactoDiretoForm(forms.ModelForm):
    class Meta:
        model = m.t_Impacto_Direto
        exclude = ('cod_Imp_Direto', )


class ImpactoIndiretoForm(forms.ModelForm):
    class Meta:
        model = m.t_Impacto_Indireto
        exclude =('cod_Imp_Indireto', )


class InfraestruturaForm(forms.ModelForm):
    class Meta:
        model = m.t_Infraestrutura
        exclude = ('cod_Infraestrutura', 'fk_Sistema', )


class ContinuidadeTecnologicaForm(forms.ModelForm):
    class Meta:
        model = m.t_Continuidade_Tecnologica
        exclude = ('cod_Continuidade', 'fk_Sistema', )


class CriticidadeForm(forms.ModelForm):
    class Meta:
        model = m.t_Criticidade
        exclude = ('cod_Criticidade', 'fk_Sistema', )


class UsuarioChaveForm(forms.ModelForm):
    class Meta:
        model = m.t_Usuario_Chave
        exclude = ('cod_Usuario_Chave', )


class ImpactoPotencialForm(forms.ModelForm):
    class Meta:
        model = m.t_Impacto_Potencial
        exclude = ('cod_Impacto_Potencial', )


class SistemaJanelasForm(forms.ModelForm):
    class Meta:
        model = m.t_Sistema_Janelas
        exclude = ('cod_Janela', )


class ImpactoNegocioForm(forms.ModelForm):
    class Meta:
        exclude = ('cod_Impacto', 'fk_Sistema', )


class ContingenciaUsuarioForm(forms.ModelForm):
    class Meta:
        model = m.t_Contingencia_Usuario
        exclude = ('cod_Nome', )


class ContingenciaForm(forms.ModelForm):
    class Meta:
        model = m.t_Contingencia
        exclude = ('cod_Contingencia', )
