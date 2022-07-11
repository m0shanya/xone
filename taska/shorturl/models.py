from django.conf import settings
from django.db import models


class Urls(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='urls', verbose_name="creator", default=''
    )
    url = models.CharField(max_length=300, verbose_name='URL')
    short = models.CharField(max_length=200, verbose_name='short')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url