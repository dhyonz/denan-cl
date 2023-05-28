from django.db import models

from django.utils.translation import gettext_lazy as _

# Create your models here.

class Unit(models.Model):
    unit_Type = models.CharField(_('Unit Type'), max_length=100, default=None, blank=True, null=True)
    unit_ID = models.CharField(_('Unit ID'), max_length=100, default=None, blank=True, null=True)
    def __str__(self):
        return f"{self.unit_ID}"
    # doc_no = models.CharField(_('Doc. No.'), max_length=15, default=None, blank=True, null=True)
    # issue_date = models.DateField(_('Issue Date'), default=None, blank=True, null=True)
    # revision_no = models.PositiveIntegerField(_('Revision No.'), default=None, blank=True, null=True)
    # def __str__(self):
    #     return f"{self.title}"