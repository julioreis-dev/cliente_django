from django.db import models


class Materia(models.Model):
    name = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('name',)
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'
