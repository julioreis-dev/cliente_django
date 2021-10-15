from django.test import TestCase
from secretaria.models import Materia
from model_mommy import mommy

class MateriaModelTest(TestCase):
    def setUp(self) -> None:
        self.materia = mommy.make('Materia')

    def test_materia_exist(self) -> None:
        mat = Materia.objects.first()
        self.assertIsNotNone(mat)

    def test_str_materia(self) -> None:
        self.assertEquals(str(self.materia), self.materia.name)
