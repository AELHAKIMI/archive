from django.forms import ModelForm
from django import forms
from .models import archive,WorkList
from django.contrib.admin.widgets import FilteredSelectMultiple
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

class ArchiveAdminForm(ModelForm):
    archive = forms.ModelMultipleChoiceField(
        queryset = archive.objects.all(),
        required = True,
        widget = FilteredSelectMultiple(
            verbose_name = 'Archives', 
            is_stacked = False,
        )
    )
    class Meta:
        model = archive
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(ArchiveAdminForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields['archive'].initial = self.instance.archive.all()
    def save(self, commit=True):
        archive = super(ArchiveAdminForm, self).save(commit=False)

        if commit:
            archive.save()

        if archive.pk:
            archive.archive = self.cleaned_data['archive']
            self.save_m2m()

        return archive


    