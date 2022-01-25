from getpass import getuser
from django.db import models
from django.utils.translation import gettext as _
from  django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(
        verbose_name=_("Author Name"),
        max_length=75
    )
    user = models.OneToOneField(
        User, 
        verbose_name=_("Associate User"), 
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(_("Created At"), auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified At"), auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")

    def __str__(self):
        return self.name
