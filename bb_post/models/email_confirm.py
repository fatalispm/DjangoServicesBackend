from django.conf import settings
from django.db import models


class EmailConfirm(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    confirmation_code = models.CharField(max_length=300)
    code_used = models.BooleanField(default=False)
