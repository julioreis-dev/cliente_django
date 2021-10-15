from secretaria.models import ENS_CHOICE
from django.db import models


class Serie(models.Model):
    ensino = models.CharField(choices=ENS_CHOICE, max_length=30, unique=True)
    # ano = models.CharField(choices=CLASS_CHOICE, default=1, max_length=30)

    def __str__(self):
        return f'{self.ensino}'

    class Meta:
        ordering = ('ensino',)
        verbose_name = 'Serie'
        verbose_name_plural = 'Series'
