from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import archive
from . import forms

# Create your views here.

class ArchiveListView(ListView):
    template_name = 'index.html'
    context_object_name = 'all_archives'
    def get_queryset(self):
        return archive.objects.all()

class ArchiveCreateView(CreateView):
    template_name = 'add.html'
    model         = archive
    form_class = forms.ArchiveForm

titles = ('Index Patient', 'Nom Patient', 'Numero Dossier', 'Description',)
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
    
    