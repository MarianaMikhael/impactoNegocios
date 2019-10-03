from django.forms import ModelForm

import systems.models as m


class CadeiaServicoForm(ModelForm):
    class Meta:
        model = m.t_Cadeia_Servico
        fields = [
            'cadeia_Servico',
        ]


class AreaDesenvolvimentoForm(ModelForm):
    class Meta:
        model = m.t_Area_Desenvolvimento
        fields = [
            'area_Dev',
            # 'gerente_Area_Dev',
            # 'coordenador_Area_Dev',
        ]


class AreaSuporteForm(ModelForm):
    class Meta:
        model = m.t_Area_Suporte
        fields = [
            'area_Sup',
            # 'gerente_Area_Sup',
            # 'coordenador_Area_Sup',
        ]


class ResponsavelDesenvolvimentoForm(ModelForm):
    class Meta:
        model = m.t_Responsavel_Desenvolvimento
        fields = [
            'nome_Resp_Dev',
            'celula_Dev',
        ]


class ResponsavelSuporteForm(ModelForm):
    class Meta:
        model = m.t_Responsavel_Suporte
        fields = [
            'nome_Resp_Sup',
            'celula_Sup',
        ]


class CriticidadeSuporteForm(ModelForm):
    class Meta:
        model = m.t_Criticidade_Suporte
        fields = [
            'nivel_Criticidade',
            'criticidade_Suporte',
        ]


class SistemaForm(ModelForm):
    class Meta:
        model = m.t_Sistema
        fields = [
            'sistema',
            'RTO_hrs',
            'servidores',
            'topologia',
        ]


class SistemaServicoForm(ModelForm):
    class Meta:
        model = m.t_Sistema_Servico
        fields = [
            'servico',
        ]


class SistemaJanelasForm(ModelForm):
    class Meta:
        model = m.t_Sistema_Janelas
        fields = [
            'janela_Critica',
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
        model = m.t_Contingencia_Arquitetura_Nome
        fields = [
            'nome_Contingencia',
        ]


class ContingenciaUsuarioForm(ModelForm):
    class Meta:
        model = m.t_Contingencia_Usuario_Nome
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
            'observacoes',
        ]


class ImpactoDependenciasForm(ModelForm):
    class Meta:
        model = m.t_Impacto_Dependencias
        fields = [
            'dependencia',
        ]


class ImpactoFronteirasForm(ModelForm):
    class Meta:
        model = m.t_Impacto_Fronteiras
        fields = [
            'fronteira',
        ]


class ImpactosPotenciaisForm(ModelForm):
    class Meta:
        model = m.t_Impacto_Potenciais
        fields = [
            'descricao_Impacto_Potencial',
        ]


class ImpactoUsuariosForm(ModelForm):
    class Meta:
        model = m.t_Impacto_Usuarios
        fields = [
            'usuario_Chave',
        ]
