from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Atividade, Modalidade


@method_decorator(login_required, name='dispatch')
class ListarEnsino(ListView):
    template_name = 'ensino/listar_ensino.html'
    model = Atividade
    context_object_name = 'atividades'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(modalidade=Modalidade.objects.get(id_modalidade=1))
        return queryset


@method_decorator(login_required, name='dispatch')
class ListarPesquisa(ListView):
    template_name = 'pesquisa/listar_pesquisa.html'
    model = Atividade
    context_object_name = 'atividades'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(modalidade=Modalidade.objects.get(id_modalidade=2))
        return queryset


@method_decorator(login_required, name='dispatch')
class ListarExtensao(ListView):
    template_name = 'extensao/listar_extensao.html'
    model = Atividade
    context_object_name = 'atividades'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(modalidade=Modalidade.objects.get(id_modalidade=3))
        return queryset


@method_decorator(login_required, name='dispatch')
class CadastrarEnsino(CreateView):
    template_name = 'ensino/cadastrar_ensino.html'
    model = Atividade
    fields = ['codigo', 'descricao', 'ch_min', 'ch_max', 'ap_max']
    success_url = reverse_lazy('listar_atividade_ensino')

    def form_valid(self, form):
        form.instance.modalidade = Modalidade.objects.get(id_modalidade=1)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Cadastrar"
        return context


@method_decorator(login_required, name='dispatch')
class CadastrarPesquisa(CreateView):
    template_name = 'pesquisa/cadastrar_pesquisa.html'
    model = Atividade
    fields = ['codigo', 'descricao', 'ch_min', 'ch_max', 'ap_max']
    success_url = reverse_lazy('listar_atividade_pesquisa')

    def form_valid(self, form):
        form.instance.modalidade = Modalidade.objects.get(id_modalidade=2)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Cadastrar"
        return context


@method_decorator(login_required, name='dispatch')
class CadastrarExtensao(CreateView):
    template_name = 'extensao/cadastrar_extensao.html'
    model = Atividade
    fields = ['codigo', 'descricao', 'ch_min', 'ch_max', 'ap_max']
    success_url = reverse_lazy('listar_atividade_extensao')

    def form_valid(self, form):
        form.instance.modalidade = Modalidade.objects.get(id_modalidade=3)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Cadastrar"
        return context


@method_decorator(login_required, name='dispatch')
class EditarEnsino(UpdateView):
    template_name = 'ensino/cadastrar_ensino.html'
    model = Atividade
    fields = ['codigo', 'descricao', 'ch_min', 'ch_max', 'ap_max']
    success_url = reverse_lazy('listar_atividade_ensino')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar"
        return context


@method_decorator(login_required, name='dispatch')
class EditarPesquisa(UpdateView):
    template_name = 'pesquisa/cadastrar_pesquisa.html'
    model = Atividade
    fields = ['codigo', 'descricao', 'ch_min', 'ch_max', 'ap_max']
    success_url = reverse_lazy('listar_atividade_pesquisa')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar"
        return context


@method_decorator(login_required, name='dispatch')
class EditarExtensao(UpdateView):
    template_name = 'extensao/cadastrar_extensao.html'
    model = Atividade
    fields = ['codigo', 'descricao', 'ch_min', 'ch_max', 'ap_max']
    success_url = reverse_lazy('listar_atividade_extensao')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Editar"
        return context


@method_decorator(login_required, name='dispatch')
class DeletarEnsino(DeleteView):
    model = Atividade
    template_name = 'ensino/excluir_ensino.html'
    success_url = reverse_lazy('listar_atividade_ensino')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Excluir"
        return context


@method_decorator(login_required, name='dispatch')
class DeletarPesquisa(DeleteView):
    model = Atividade
    template_name = 'pesquisa/excluir_pesquisa.html'
    success_url = reverse_lazy('listar_atividade_pesquisa')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Excluir"
        return context


@method_decorator(login_required, name='dispatch')
class DeletarExtensao(DeleteView):
    model = Atividade
    template_name = 'extensao/excluir_extensao.html'
    success_url = reverse_lazy('listar_atividade_extensao')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Excluir"
        return context
