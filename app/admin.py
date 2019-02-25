from django.contrib import admin
from .models import archive, WorkList
from .forms import ArchiveAdminForm
# Register your models here.

admin.site.register(archive)


class WorkListAdmin(admin.ModelAdmin):
    form = ArchiveAdminForm

admin.site.register(WorkList, WorkListAdmin)