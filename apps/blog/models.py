from django.db import models
from django.utils.translation import gettext as _

class Post(models.Model):
    title = models.CharField(_("Title"), max_length=75)
    content = models.TextField(_("Content"))
    created_by = models.ForeignKey(
        "users.Author", 
        verbose_name=_("Created By"), 
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(_("Created At"), auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified At"), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title

