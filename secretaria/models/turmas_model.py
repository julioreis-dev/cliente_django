from secretaria.models import STRING_CHOICE, TURNO_CHOICE
from secretaria.models.professores_model import Professor
from secretaria.models.series_model import Serie
from django.db import models
import datetime

year = datetime.date.today().year


class Turma(models.Model):
    serie = models.ForeignKey(Serie, null=True, blank=True, on_delete=models.CASCADE)
    prof = models.ManyToManyField(Professor, help_text='Escolha os professores e transfira para a tabela da direita. ',
                                  blank=True, verbose_name="Professor")
    classe = models.CharField(choices=STRING_CHOICE, max_length=100, default='Alfa')
    turno = models.CharField(choices=TURNO_CHOICE, max_length=100, default='Manha')
    ano = models.IntegerField(verbose_name="Ano da turma", help_text=f'ex:{year}', default=year)

    # aluno = models.ForeignKey(Aluno, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.serie}-{self.classe}-{self.turno}-{self.ano}'

    class Meta:
        ordering = ('-ano',)
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
