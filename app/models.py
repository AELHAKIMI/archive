from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator
# Create your models here.

class archive(models.Model):
    index_patient  = models.PositiveIntegerField(verbose_name='Index Patient', unique=True)
    nom_patient    = models.CharField(max_length=128,verbose_name='Nom Patient' )
    num_dossier    = models.CharField(max_length=64, verbose_name='Numero Dossier')
    description    = models.TextField(max_length=1000, verbose_name='Description', blank=True)
    def __str__(self):
        return str(self.index_patient) + ' - '  + self.nom_patient + ' - ' + self.num_dossier
    def get_absolute_url(self):
        return reverse('detail-view', kwargs={'pk': self.pk})

class WorkList(models.Model):
    date_worklist   = models.DateField(verbose_name='Date Worklist', auto_now=False)
    archive         = models.ManyToManyField(archive, verbose_name='Archive', related_name='archives')
    description     = models.TextField(max_length=1000, verbose_name='Description',blank=True)

    def __str__(self):
        return  str(self.date_worklist) 
    
    def get_absolute_url(self):
        return reverse('worklist-detail-view', kwargs={'pk': self.pk})