from django.db import models


class Urls(models.Model):
    url = models.CharField(max_length=300, verbose_name='long')
    short = models.CharField(max_length=200, verbose_name='short')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url