from django.db import models

from units.models import Unit
from crew.models import Crew

from django.utils.translation import gettext_lazy as _

# Create your models here.

# class MaintenanceForm(models.Model):
class PreventiveWO(models.Model):
    title = models.CharField(_('Title'), max_length=100, default=None, blank=True, null=True)
    doc_no = models.CharField(_('Doc. No.'), max_length=15, default=None, blank=True, null=True)
    issue_date = models.DateField(_('Issue Date'), default=None, blank=True, null=True)
    revision_no = models.PositiveIntegerField(_('Revision No.'), default=None, blank=True, null=True)
    unit_No = models.ForeignKey(Unit, on_delete=models.CASCADE, default=None, blank=True, null=True)
    wo_No = models.CharField(_('WO No.'), max_length=100, default=None, blank=True, null=True)
    pm_No = models.CharField(_('PM No.'), max_length=7, default='1407', blank=True, null=True)
    time_Start = models.TimeField(_('Time Start'), default=None, blank=True, null=True)
    time_Finish = models.TimeField(_('Time Finish'), default=None, blank=True, null=True)
    pic_Officer = models.ForeignKey(Crew, on_delete=models.CASCADE, default=None, blank=True, null=True)
    # pic_Officer = models
    def __str__(self):
        return f"{self.title}"