from django.contrib import admin

from .models import *

class PreventiveWOAdmin(admin.ModelAdmin):
    list_display_links = ('title',)
    list_display = ('title', 'pic_Officer', 'doc_no', 'issue_date', 'time_Start', 'time_Finish', 'revision_no', 'unit_No')

# Register your models here.

admin.site.register(PreventiveWO, PreventiveWOAdmin)