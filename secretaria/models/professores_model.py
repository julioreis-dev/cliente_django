from secretaria.models.series_model import Serie
from secretaria.models.disciplinas_model import Materia
from django.db import models


class Professor(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nome")
    sobrenome = models.CharField(max_length=150)
    admissao = models.DateField(verbose_name="Data de admissão", auto_now_add=True, null=True)
    disciplina = models.ManyToManyField(Materia,
                                        blank=True,
                                        help_text='Escolha as disciplinas ministradas '
                                                  'pelo professor e transfira para a tabela da direita.')
    # serie_turma = models.ManyToManyField(Serie, blank=True)

    def __str__(self):
        return f'{self.name} {self.sobrenome}'

    class Meta:
        ordering = ('name',)
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
