from django.contrib import admin
from . import models
# Register your models here.
class DatasetAdmin(admin.ModelAdmin):
    list_display = [f.name for f in models.Dataset._meta.fields]
admin.site.register(models.Dataset, DatasetAdmin)