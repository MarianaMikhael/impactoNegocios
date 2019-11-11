from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from django.contrib.auth.decorators import login_required


from systems import models as m
from .forms import form_cadastro as f


def ac(request):
    data = {}
    data['cadeia_servico'] = m.t_Cadeia_Servico.objects.all()
    data['resp_desenvolvimento'] = m.t_Responsavel_Desenvolvimento.objects.all()
    data['resp_suporte'] = m.t_Responsavel_Suporte.objects.all()
    data['sistema'] = m.t_Sistema.objects.all()
    data['cont_tecnologica'] = m.t_Continuidade_Tecnologica.objects.all()
    data['criticidade'] = m.t_Criticidade.objects.filter(nivel_Criticidade='AC') 
    data['imp_direto'] = m.t_Impacto_Direto.objects.all()
    data['imp_Indireto'] = m.t_Impacto_Indireto.objects.all()
    data['infraestrutura'] = m.t_Infraestrutura.objects.all()
    data['usuario_chave'] = m.t_Usuario_Chave.objects.all()
    data['imp_potencial'] = m.t_Impacto_Potencial.objects.all()
    data['sistema_janela'] = m.t_Sistema_Janelas.objects.all()   
    data['imp_negocio'] = m.t_Impacto_Negocio.objects.all()
    data['contin_usuario'] = m.t_Contingencia_Usuario.objects.all()
    data['contingencia'] = m.t_Contingencia.objects.all()
    return render(request, 'systems/index.html', data)


def acn(request):
    data = {}
    data['cadeia_servico'] = m.t_Cadeia_Servico.objects.all()
    data['resp_desenvolvimento'] = m.t_Responsavel_Desenvolvimento.objects.all()
    data['resp_suporte'] = m.t_Responsavel_Suporte.objects.all()
    data['sistema'] = m.t_Sistema.objects.all()
    data['cont_tecnologica'] = m.t_Continuidade_Tecnologica.objects.all()
    data['criticidade'] = m.t_Criticidade.objects.filter(nivel_Criticidade='ACN') 
    data['imp_direto'] = m.t_Impacto_Direto.objects.all()
    data['imp_Indireto'] = m.t_Impacto_Indireto.objects.all()
    data['infraestrutura'] = m.t_Infraestrutura.objects.all()
    data['usuario_chave'] = m.t_Usuario_Chave.objects.all()
    data['imp_potencial'] = m.t_Impacto_Potencial.objects.all()
    data['sistema_janela'] = m.t_Sistema_Janelas.objects.all()   
    data['imp_negocio'] = m.t_Impacto_Negocio.objects.all()
    data['contin_usuario'] = m.t_Contingencia_Usuario.objects.all()
    data['contingencia'] = m.t_Contingencia.objects.all()
    return render(request, 'systems/index.html', data)
    

def acn_plus(request):
    data = {}
    data['cadeia_servico'] = m.t_Cadeia_Servico.objects.all()
    data['resp_desenvolvimento'] = m.t_Responsavel_Desenvolvimento.objects.all()
    data['resp_suporte'] = m.t_Responsavel_Suporte.objects.all()
    data['sistema'] = m.t_Sistema.objects.all()
    data['cont_tecnologica'] = m.t_Continuidade_Tecnologica.objects.all()
    data['criticidade'] = m.t_Criticidade.objects.filter(nivel_Criticidade='ACN+') 
    data['imp_direto'] = m.t_Impacto_Direto.objects.all()
    data['imp_Indireto'] = m.t_Impacto_Indireto.objects.all()
    data['infraestrutura'] = m.t_Infraestrutura.objects.all()
    data['usuario_chave'] = m.t_Usuario_Chave.objects.all()
    data['imp_potencial'] = m.t_Impacto_Potencial.objects.all()
    data['sistema_janela'] = m.t_Sistema_Janelas.objects.all()   
    data['imp_negocio'] = m.t_Impacto_Negocio.objects.all()
    data['contin_usuario'] = m.t_Contingencia_Usuario.objects.all()
    data['contingencia'] = m.t_Contingencia.objects.all()
    return render(request, 'systems/index.html', data)


@login_required
def create_sistema(request):
    detalhamentos = {}
    form_cadeia_servico = f.CadeiaServicoForm(
        request.POST or None, request.FILES or None)
    form_responsavel_desenvolvimento = f.ResponsavelDesenvolvimentoForm(
        request.POST or None, request.FILES or None)
    form_responsavel_suporte = f.ResponsavelSuporteForm(
        request.POST or None, request.FILES or None)
    form_sistema = f.SistemaForm(
        request.POST or None, request.FILES or None) 
    form_cont_tecnologica = f.ContinuidadeTecnologicaForm(
        request.POST or None, request.FILES or None) 
    form_criticidade = f.CriticidadeForm(
        request.POST or None, request.FILES or None)
    form_imp_direto = f.ImpactoDiretoForm(
        request.POST or None, request.FILES or None)
    form_imp_indireto = f.ImpactoIndiretoForm(
        request.POST or None, request.FILES or None)    
    form_infraestrutura = f.InfraestruturaForm(
        request.POST or None, request.FILES or None)
    form_usuario_chave = f.UsuarioChaveForm(
        request.POST or None, request.FILES or None)
    form_imp_potencial = f.ImpactoPotencialForm(
        request.POST or None, request.FILES or None)
    form_sistema_janelas = f.SistemaJanelasForm(
        request.POST or None, request.FILES or None)    
    form_imp_negocio = f.ImpactoNegocioForm(
        request.POST or None, request.FILES or None)
    form_contin_usuario = f.ContingenciaUsuarioForm(
        request.POST or None, request.FILES or None)
    form_contingencia = f.ContingenciaForm(
        request.POST or None, request.FILES or None)

    if (
        form_cadeia_servico.is_valid() and
        form_responsavel_desenvolvimento.is_valid() and
        form_responsavel_suporte.is_valid() and
        form_sistema.is_valid() and
        form_cont_tecnologica.is_valid() and
        form_criticidade.is_valid() and
        form_imp_direto.is_valid() and
        form_imp_indireto.is_valid() and
        form_infraestrutura.is_valid() and
        form_usuario_chave.is_valid() and
        form_imp_potencial.is_valid() and
        form_sistema_janelas.is_valid() and
        form_imp_negocio.is_valid() and
        form_contin_usuario.is_valid() and
        form_contingencia.is_valid()
    ):

        form_cadeia_servico.save()
        form_responsavel_desenvolvimento.save()
        form_responsavel_suporte.save()
        form_sistema.save()
        form_cont_tecnologica.save()
        form_criticidade.save()
        form_imp_direto.save()
        form_imp_indireto.save()
        form_infraestrutura.save()
        form_usuario_chave.save()
        form_imp_potencial.save()
        form_sistema_janelas.save()
        form_imp_negocio.save()
        form_contin_usuario.save()
        form_contingencia.save()
        return redirect('home')

    detalhamentos[
        'form_cadeia_servico'] = form_cadeia_servico
    detalhamentos[
        'form_responsavel_desenvolvimento'] = form_responsavel_desenvolvimento
    detalhamentos[
        'form_responsavel_suporte'] = form_responsavel_suporte
    detalhamentos[
        'form_sistema'] = form_sistema
    detalhamentos[
        'form_cont_tecnologica'] = form_cont_tecnologica
    detalhamentos[
        'form_criticidade'] = form_criticidade
    detalhamentos[
        'form_imp_direto'] = form_imp_direto
    detalhamentos[
        'form_imp_indireto'] = form_imp_indireto
    detalhamentos[
        'form_infraestrutura'] = form_infraestrutura
    detalhamentos[
        'form_usuario_chave'] = form_usuario_chave
    detalhamentos[
        'form_imp_potencial'] = form_imp_potencial
    detalhamentos[
        'form_sistema_janelas'] = form_sistema_janelas
    detalhamentos[
        'form_imp_negocio'] = form_imp_negocio
    detalhamentos[
        'form_contin_usuario'] = form_contin_usuario
    detalhamentos[
        'form_contingencia'] = form_contingencia
    return render(request, 'systems/forms/form-system.html', detalhamentos)


@login_required
def update_sistema(request, cod_Sistema):
    sistema = get_object_or_404(m.t_Sistema, pk=cod_Sistema)
    form = [
        f.CadeiaServicoForm(request.POST or None, request.FILES or None, instance=sistema),
        f.ResponsavelDesenvolvimentoForm(request.POST or None, request.FILES or None, instance=sistema),
        f.ResponsavelSuporteForm(request.POST or None, request.FILES or None, instance=sistema),
        f.SistemaForm(request.POST or None, request.FILES or None, instance=sistema),
        f.ContinuidadeTecnologicaForm(request.POST or None, request.FILES or None, instance=sistema),
        f.CriticidadeForm(request.POST or None, request.FILES or None, instance=sistema),
        f.ImpactoDiretoForm(request.POST or None, request.FILES or None, instance=sistema),
        f.ImpactoIndiretoForm(request.POST or None, request.FILES or None, instance=sistema),
        f.InfraestruturaForm(request.POST or None, request.FILES or None, instance=sistema),
        f.UsuarioChaveForm(request.POST or None, request.FILES or None, instance=sistema),
        f.ImpactoPotencialForm(request.POST or None, request.FILES or None, instance=sistema),
        f.SistemaJanelasForm(request.POST or None, request.FILES or None, instance=sistema),
        f.ImpactoNegocioForm(request.POST or None, request.FILES or None, instance=sistema),
        f.ContingenciaUsuarioForm(request.POST or None, request.FILES or None, instance=sistema),
        f.ContingenciaForm(request.POST or None, request.FILES or None, instance=sistema),
    ]

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'systems/form.html', {'form': form})


@login_required
def delete_sistema(request, cod_Sistema):
    sistema = get_object_or_404(m.t_Sistema, pk=cod_Sistema)

    if request.method == 'POST':
        sistema.delete()
        return redirect('home')

    return render(request, 'systems/form_delete_confirmation.html', {'sistema': sistema})
