from django.test import TestCase
from secretaria.models import Serie
from model_mommy import mommy

class SerieModelTest(TestCase):
    def setUp(self) -> None:
        self.serie = mommy.make('Serie')

    def test_serie_exist(self) -> None:
        serie = Serie.objects.first()
        self.assertIsNotNone(serie)

    def test_str_serie(self) -> None:
        self.assertEquals(str(self.serie), str(self.serie.ensino))
