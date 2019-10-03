from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from django.contrib.auth.decorators import login_required


import systems.models as m
from .forms import form_cadastro as f


@login_required
def index(request):
    data = {}
    data['cadeia_servico'] = m.t_Cadeia_Servico.objects.all()
    data['area_desenvolvimento'] = m.t_Area_Desenvolvimento.objects.all()
    data['area_suporte'] = m.t_Area_Suporte.objects.all()
    data['resp_desenvolvimento'] = m.t_Responsavel_Desenvolvimento.objects.all()
    data['resp_suporte'] = m.t_Responsavel_Suporte.objects.all()
    data['criticidade_sup'] = m.t_Criticidade_Suporte.objects.all()
    data['sistemas'] = m.t_Sistema.objects.all()
    data['sistema_servico'] = m.t_Sistema_Servico.objects.all()
    data['sistema_janela'] = m.t_Sistema_Janelas.objects.all()
    data['contingencias'] = m.t_Contingencia.objects.all()
    data['cont_arquitetura'] = m.t_Contingencia_Arquitetura_Nome.objects.all()
    data['cont_usuario'] = m.t_Contingencia_Usuario_Nome.objects.all()
    data['cont_tecnologica'] = m.t_Continuidade_Tecnologica.objects.all()
    data['cont_sites'] = m.t_Continuidade_Tecnologica_Sites.objects.all()
    data['impactos'] = m.t_Impacto.objects.all()
    data['imp_dependencias'] = m.t_Impacto_Dependencias.objects.all()
    data['imp_fronteiras'] = m.t_Impacto_Fronteiras.objects.all()
    data['imp_potenciais'] = m.t_Impacto_Potenciais.objects.all()
    data['usuario_chave'] = m.t_Impacto_Usuarios.objects.all()
    return render(request, 'sistemas/index.html', data)


@login_required
def create_sistema(request):
    detalhamentos = {}
    form_cadeia_servico = f.CadeiaServicoForm(
        request.POST or None, request.FILES or None)
    form_area_desenvolvimento = f.AreaDesenvolvimentoForm(
        request.POST or None, request.FILES or None)
    form_area_suporte = f.AreaSuporteForm(
        request.POST or None, request.FILES or None)
    form_responsavel_desenvolvimento = f.ResponsavelDesenvolvimentoForm(
        request.POST or None, request.FILES or None)
    form_responsavel_suporte = f.ResponsavelSuporteForm(
        request.POST or None, request.FILES or None)
    form_criticidade_suporte = f.CriticidadeSuporteForm(
        request.POST or None, request.FILES or None)
    form_sistema = f.SistemaForm(
        request.POST or None, request.FILES or None)
    form_sistema_servico = f.SistemaServicoForm(
        request.POST or None, request.FILES or None)
    form_sistema_janelas = f.SistemaJanelasForm(
        request.POST or None, request.FILES or None)
    form_contingencia = f.ContingenciaForm(
        request.POST or None, request.FILES or None)
    form_contingencia_arquitetura = f.ContingenciaArquiteturaForm(
        request.POST or None, request.FILES or None)
    form_contingencia_usuario = f.ContingenciaUsuarioForm(
        request.POST or None, request.FILES or None)
    form_continuidade_tecnologica = f.ContinuidadeTecnologicaForm(
        request.POST or None, request.FILES or None)
    form_cont_tecnologica_sites = f.ContinuidadeTecnologicaSitesForm(
        request.POST or None, request.FILES or None)
    form_impacto = f.ImpactoForm(
        request.POST or None, request.FILES or None)
    form_impacto_dependencias = f.ImpactoDependenciasForm(
        request.POST or None, request.FILES or None)
    form_impacto_fronteiras = f.ImpactoFronteirasForm(
        request.POST or None, request.FILES or None)
    form_impactos_potenciais = f.ImpactosPotenciaisForm(
        request.POST or None, request.FILES or None)
    form_impacto_usuarios = f.ImpactoUsuariosForm(
        request.POST or None, request.FILES or None)

    if (
        form_cadeia_servico.is_valid() and
        form_area_desenvolvimento.is_valid() and
        form_area_suporte.is_valid() and
        form_responsavel_desenvolvimento.is_valid() and
        form_responsavel_suporte.is_valid() and
        form_criticidade_suporte.is_valid() and
        form_sistema.is_valid() and
        form_sistema_servico.is_valid() and
        form_sistema_janelas.is_valid() and
        form_contingencia.is_valid() and
        form_contingencia_arquitetura.is_valid() and
        form_contingencia_usuario.is_valid() and
        form_continuidade_tecnologica.is_valid() and
        form_cont_tecnologica_sites.is_valid() and
        form_impacto.is_valid() and
        form_impacto_dependencias.is_valid() and
        form_impacto_fronteiras.is_valid() and
        form_impactos_potenciais.is_valid() and
        form_impacto_usuarios.is_valid()
    ):

        form_cadeia_servico.save()
        form_area_desenvolvimento.save()
        form_area_suporte.save()
        form_responsavel_desenvolvimento.save()
        form_responsavel_suporte.save()
        form_criticidade_suporte.save()
        form_sistema.save()
        form_sistema_servico.save()
        form_sistema_janelas.save()
        form_contingencia.save()
        form_contingencia_arquitetura.save()
        form_contingencia_usuario.save()
        form_continuidade_tecnologica.save()
        form_cont_tecnologica_sites.save()
        form_impacto.save()
        form_impacto_dependencias.save()
        form_impacto_fronteiras.save()
        form_impactos_potenciais.save()
        form_impacto_usuarios.save()
        return redirect('index_sistemas')

    detalhamentos[
        'form_cadeia_servico'] = form_cadeia_servico
    detalhamentos[
        'form_area_desenvolvimento'] = form_area_desenvolvimento
    detalhamentos[
        'form_area_suporte'] = form_area_suporte
    detalhamentos[
        'form_responsavel_desenvolvimento'] = form_responsavel_desenvolvimento
    detalhamentos[
        'form_responsavel_suporte'] = form_responsavel_suporte
    detalhamentos[
        'form_criticidade_suporte'] = form_criticidade_suporte
    detalhamentos[
        'form_sistema'] = form_sistema
    detalhamentos[
        'form_sistema_servico'] = form_sistema_servico
    detalhamentos[
        'form_sistema_janelas'] = form_sistema_janelas
    detalhamentos[
        'form_contingencia'] = form_contingencia
    detalhamentos[
        'form_contingencia_arquitetura'] = form_contingencia_arquitetura
    detalhamentos[
        'form_contingencia_usuario'] = form_contingencia_usuario
    detalhamentos[
        'form_continuidade_tecnologica'] = form_continuidade_tecnologica
    detalhamentos[
        'form_cont_tecnologica_sites'] = form_cont_tecnologica_sites
    detalhamentos[
        'form_impacto'] = form_impacto
    detalhamentos[
        'form_impacto_dependencias'] = form_impacto_dependencias
    detalhamentos[
        'form_impacto_fronteiras'] = form_impacto_fronteiras
    detalhamentos[
        'form_impactos_potenciais'] = form_impactos_potenciais
    detalhamentos[
        'form_impacto_usuarios'] = form_impacto_usuarios
    return render(request, 'sistemas/form.html', detalhamentos)


@login_required
def update_sistema(request, cod_Sistema):
    sistema = get_object_or_404(m.t_Sistema, pk=cod_Sistema)
    form = [
        f.CadeiaServicoForm(request.POST or None, request.FILES or None, instance=sistema),
        f.AreaDesenvolvimentoForm(request.POST or None, request.FILES or None, instance=sistema),
        f.AreaSuporteForm(request.POST or None, request.FILES or None, instance=sistema),
        f.ResponsavelDesenvolvimentoForm(request.POST or None, request.FILES or None, instance=sistema),
        f.ResponsavelSuporteForm(request.POST or None, request.FILES or None, instance=sistema),
        f.CriticidadeSuporteForm(request.POST or None, request.FILES or None, instance=sistema),
        f.SistemaForm(request.POST or None, request.FILES or None, instance=sistema),
        f.SistemaServicoForm(request.POST or None, request.FILES or None, instance=sistema),
        f.SistemaJanelasForm(request.POST or None, request.FILES or None, instance=sistema),
        f.ContingenciaForm(request.POST or None, request.FILES or None, instance=sistema),
        f.ContingenciaArquiteturaForm(request.POST or None, request.FILES or None, instance=sistema),
        f.ContingenciaUsuarioForm(request.POST or None, request.FILES or None, instance=sistema),
        f.ContinuidadeTecnologicaForm(request.POST or None, request.FILES or None, instance=sistema),
        f.ContinuidadeTecnologicaSitesForm(request.POST or None, request.FILES or None, instance=sistema),
        f.ImpactoForm(request.POST or None, request.FILES or None, instance=sistema)
    ]

    if form.is_valid():
        form.save()
        return redirect('index_sistemas')

    return render(request, 'sistemas/form.html', {'form': form})


@login_required
def delete_sistema(request, cod_Sistema):
    sistema = get_object_or_404(m.t_Sistema, pk=cod_Sistema)

    if request.method == 'POST':
        sistema.delete()
        return redirect('index_sistemas')

    return render(request, 'sistemas/form_delete_confirmation.html', {'sistema': sistema})
