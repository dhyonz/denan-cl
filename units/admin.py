from django.contrib import admin

from .models import *

# class UnitsAdmin(admin.ModelAdmin):
    # list_display_links = ('title',)
    # list_display = ('title', 'doc_no', 'issue_date', 'revision_no')

# Register your models here.

admin.site.register(Unit)