from django.forms import ModelForm

import systems.models as m


class CadeiaServicoForm(ModelForm):
    class Meta:
        model = m.t_Cadeia_Servico
        fields = [
            # 'cadeia_Servico',
        ]


class AreaDesenvolvimentoForm(ModelForm):
    class Meta:
        model = m.t_Area_Desenvolvimento
        fields = [
            # 'area_Dev',
            # 'gerente_Area_Dev',
            # 'coordenador_Area_Dev',
        ]


class AreaSuporteForm(ModelForm):
    class Meta:
        model = m.t_Area_Suporte
        fields = [
            # 'area_Sup',
            # 'gerente_Area_Sup',
            # 'coordenador_Area_Sup',
        ]


class ResponsavelDesenvolvimentoForm(ModelForm):
    class Meta:
        model = m.t_Responsavel_Desenvolvimento
        fields = [
            'celula_Dev',
            'nome_Resp_Dev',
        ]


class ResponsavelSuporteForm(ModelForm):
    class Meta:
        model = m.t_Responsavel_Suporte
        fields = [
            'celula_Sup',
            'nome_Resp_Sup',
        ]


class CriticidadeForm(ModelForm):
    class Meta:
        model = m.t_Criticidade
        fields = [
            # 'nivel_Criticidade',
            # 'criticidade_Suporte',
        ]


class SistemaServicoForm(ModelForm):
    class Meta:
        model = m.t_Sistema_Servico
        fields = [
            # 'servico',
        ]


class SistemaJanelasForm(ModelForm):
    class Meta:
        model = m.t_Sistema_Janelas
        fields = [
            # 'janela_Critica',
        ]


class SistemaForm(ModelForm):
    class Meta:
        model = m.t_Sistema
        fields = [
            'sistema',
            'servicos',
            'janelas_Criticas',
            'RTO_hrs',
            'servidores',
            'url_Topologia',
        ]


class ContingenciaForm(ModelForm):
    class Meta:
        model = m.t_Contingencia
        fields = [
            'contingencia_Arquitetura',
            'contingencia_Usuario',
            'RTO_Contingencia',
        ]


class ContingenciaArquiteturaForm(ModelForm):
    class Meta:
        model = m.t_Contingencia_Arquitetura
        fields = [
            'nome_Contingencia',
        ]


class ContingenciaUsuarioForm(ModelForm):
    class Meta:
        model = m.t_Contingencia_Usuario
        fields = [
            'nome_Contingencia'
        ]


class ContinuidadeTecnologicaForm(ModelForm):
    class Meta:
        model = m.t_Continuidade_Tecnologica
        fields = [
            'continuidade_Tecnologica',
            'plano_De_Recup_Doc',
            'plano_De_Recup_Test',
            'url_Ficheiro',
        ]


class ContinuidadeTecnologicaSitesForm(ModelForm):
    class Meta:
        model = m.t_Continuidade_Tecnologica_Sites
        fields = [
            'camada',
            'servico',
            'site',
            'observacao',
        ]


class ImpactoFronteiraForm(ModelForm):
    class Meta:
        model = m.t_Impacto_Fronteira
        fields = [
            # 'fronteira',
        ]


class ImpactoDependenciaForm(ModelForm):
    class Meta:
        model = m.t_Impacto_Dependencia
        fields = [
            # 'dependencia',
        ]


class ImpactoUsuarioForm(ModelForm):
    class Meta:
        model = m.t_Impacto_Usuario
        fields = [
            # 'usuario_Chave',
        ]


class ImpactoPotencialForm(ModelForm):
    class Meta:
        model = m.t_Impacto_Potencial
        fields = [
            # 'impacto_Potencial',
        ]


class ImpactoForm(ModelForm):
    class Meta:
        model = m.t_Impacto
        fields = [
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
            'fronteiras',
            'dependencias',
            'usuario_Chave',
            'impactos_Potenciais',
            'observacoes',
        ]
