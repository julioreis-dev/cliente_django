from django.db import models
from secretaria.models.boletim_model import Boletim
from secretaria.models.disciplinas_model import Materia
from secretaria.models.alunos_model import Aluno
from secretaria.models.turmas_model import Turma


class Nota(models.Model):
    boletim = models.ForeignKey(Boletim, blank=True, on_delete=models.CASCADE, null=True)
    materia = models.ForeignKey(Materia, blank=True, on_delete=models.CASCADE, null=True)
    nota1 = models.FloatField(default=0)
    nota2 = models.FloatField(default=0)
    nota3 = models.FloatField(default=0)
    media = models.FloatField(default=0)

    def __str__(self):
        return f'{self.boletim}'
