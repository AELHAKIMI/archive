from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import archive , WorkList
from . import forms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

titles = ('Index Patient', 'Nom Patient', 'Numero Dossier', 'Description',)
class ArchiveListView(LoginRequiredMixin, ListView):
    login_url ='/login/'
    
    template_name = 'app/index.html'
    context_object_name = 'all_archives'
    def get_queryset(self):
        return archive.objects.all()
    def get_context_data(self , **kwargs):
        context = super(ArchiveListView, self).get_context_data(**kwargs)
        context.update({
            'titles' : titles,
        })
        return context

class ArchiveCreateView(LoginRequiredMixin, CreateView):
    login_url ='/login/'
    template_name = 'app/add.html'
    model         = archive
    form_class = forms.ArchiveForm


class ArchiveDetailView(LoginRequiredMixin, DetailView):
    login_url ='/login/'
    model = archive
    template_name = 'app/detail.html'
    context_object_name = 'archive'
    def get_context_data(self , **kwargs):
        context = super(ArchiveDetailView, self).get_context_data(**kwargs)
        context.update({
            'titles' : titles,
        })
        return context

class ArchiveUpdateView(LoginRequiredMixin, UpdateView):
    login_url ='/login/'
    model = archive
    template_name = 'app/add.html'
    form_class = forms.ArchiveForm
class ArchiveDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'app/confirm_delete.html'
    model         = archive
    success_url = reverse_lazy('index-view')


class WorklistListView(LoginRequiredMixin, ListView):
    login_url ='/login/'
    template_name = 'app/worklist/index.html'
    context_object_name = 'all_worklist'
    def get_queryset(self):
        return WorkList.objects.all()
    def get_context_data(self , **kwargs):
        context = super(WorklistListView, self).get_context_data(**kwargs)
        context.update({
            'titles' : titles,
        })
        return context

class WorkListCreateView(LoginRequiredMixin, CreateView):
    login_url ='/login/'
    template_name = 'app/worklist/add.html'
    model         = WorkList
    fields = '__all__'
    

class WorkListDetailView(LoginRequiredMixin, DetailView):
    login_url ='/login/'
    model = WorkList
    template_name = 'app/worklist/detail.html'
    context_object_name = 'worklist'
    def get_context_data(self , **kwargs):
        context = super(WorkListDetailView, self).get_context_data(**kwargs)
        context.update({
            'titles' : titles,
        })
        return context