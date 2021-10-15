from django.db import models
from secretaria.models.turmas_model import Turma
from secretaria.models.alunos_model import Aluno
# from secretaria.models.notas_model import Nota



class Boletim(models.Model):
    aluno = models.ForeignKey(Aluno, blank=True, on_delete=models.CASCADE, null=True)
    turma = models.ForeignKey(Turma, blank=True, on_delete=models.CASCADE, null=True)



    def __str__(self):
        return f'{self.aluno} {self.turma}'

    class Meta:
        ordering = ('aluno',)
        verbose_name = 'Boletim'
        verbose_name_plural = 'Boletins'
