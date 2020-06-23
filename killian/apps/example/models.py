from django.db import models
from django.utils.translation import ugettext_lazy as _


class Example(models.Model):
    name = models.CharField(_("Name"), max_length=128)
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date Updated"), auto_now=True)

    class Meta:
        app_label = 'example'
        verbose_name = _('Example')
        verbose_name_plural = _('Examples')

    def __str__(self):
        return self.name
