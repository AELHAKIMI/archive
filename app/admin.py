from django.contrib import admin
from .models import archive, WorkList

# Register your models here.

admin.site.register(archive)


class WorkListModelAdmin(admin.ModelAdmin):
    filter_horizontal = ["archive"]
    
    

admin.site.register(WorkList, WorkListModelAdmin) 