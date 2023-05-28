from django.db import models

from django.utils.translation import gettext_lazy as _

# Create your models here.

class Crew(models.Model):
    crew_Name = models.CharField(_('Cerw Name'), max_length=100, default=None, blank=True, null=True)
    def __str__(self):
        return f"{self.crew_Name}"