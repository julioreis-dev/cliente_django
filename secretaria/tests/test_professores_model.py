from django.test import TestCase
from secretaria.models import Professor
from model_mommy import mommy

class ProfessorModelTest(TestCase):
    def setUp(self) -> None:
        self.professor = mommy.make('Professor')

    def test_professor_exist(self) -> None:
        prof = Professor.objects.first()
        self.assertIsNotNone(prof)

    def test_str_professor(self) -> None:
        strprof = f'{self.professor.name} {self.professor.sobrenome}'
        self.assertEquals(str(self.professor), strprof)
