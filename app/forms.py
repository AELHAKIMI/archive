from django.forms import ModelForm
from django import forms
from .models import archive

class ArchiveForm(ModelForm):
    class  Meta:
        model = archive
        fields = '__all__'
        widgets = {
            'index_patient' : forms.TextInput(attrs={'class': 'form-control'}),
            'nom_patient' :forms.TextInput(attrs={'class': 'form-control'}),
            'num_dossier' :forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
        }
        