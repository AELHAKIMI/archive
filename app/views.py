from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import archive , WorkList
from . import forms
from django.urls import reverse_lazy

# Create your views here.

titles = ('Index Patient', 'Nom Patient', 'Numero Dossier', 'Description',)
class ArchiveListView(ListView):
    template_name = 'index.html'
    context_object_name = 'all_archives'
    def get_queryset(self):
        return archive.objects.all()
    def get_context_data(self , **kwargs):
        context = super(ArchiveListView, self).get_context_data(**kwargs)
        context.update({
            'titles' : titles,
        })
        return context

class ArchiveCreateView(CreateView):
    template_name = 'add.html'
    model         = archive
    form_class = forms.ArchiveForm


class ArchiveDetailView(DetailView):
    
    model = archive
    template_name = 'detail.html'
    context_object_name = 'archive'
    def get_context_data(self , **kwargs):
        context = super(ArchiveDetailView, self).get_context_data(**kwargs)
        context.update({
            'titles' : titles,
        })
        return context

class ArchiveUpdateView(UpdateView):
    model = archive
    template_name = 'add.html'
    form_class = forms.ArchiveForm
class ArchiveDeleteView(DeleteView):
    template_name = 'confirm_delete.html'
    model         = archive
    success_url = reverse_lazy('index-view')


class WorklistListView(ListView):
    template_name = 'worklist/index.html'
    context_object_name = 'all_worklist'
    def get_queryset(self):
        return WorkList.objects.all()
    def get_context_data(self , **kwargs):
        context = super(WorklistListView, self).get_context_data(**kwargs)
        context.update({
            'titles' : titles,
        })
        return context

class WorkListCreateView(CreateView):
    template_name = 'worklist/add.html'
    model         = WorkList
    fields = '__all__'
    model = archive
    