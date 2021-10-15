from django.test import TestCase
from secretaria.models import Turma
from model_mommy import mommy

class TurmaModelsTest(TestCase):
    def setUp(self) -> None:
        self.turma = mommy.make('Turma')

    def test_turma_exist(self) -> None:
        turma= Turma.objects.first()
        self.assertIsNotNone(turma)

    def test_str_turma(self) -> None:
        strturma = f'{self.turma.serie}-{self.turma.classe}-{self.turma.turno}-{self.turma.ano}'
        self.assertEquals(str(self.turma), strturma)
