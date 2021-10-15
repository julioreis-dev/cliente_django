ENS_CHOICE = [
    ('Educacao Infantil',(
                ('EI-CRE', 'EI-Creche'),
                ('EI-GP1', 'EI-Grupo 1'),
                ('EI-GP2', 'EI-Grupo 2'),
                ('EI-GP3', 'EI-Grupo 3'),
                ('EI-GP4', 'EI-Grupo 4'),
                ('EI-GP5', 'EI-Grupo 5'),)
     ),
    ('Educacao Fundamental I', (
                ('1-EFI', '1º Ano EFI'),
                ('2-EFI', '2º Ano EFI'),
                ('3-EFI', '3º Ano EFI'),
                ('4-EFI', '4º Ano EFI'),
                ('5-EFI', '5º Ano EFI'),)
     ),
    ('Educacao Fundamental II',(
                ('6-EFII', '6º Ano EFII'),
                ('7-EFII', '7º Ano EFII'),
                ('8-EFII', '8º Ano EFII'),
                ('9-EFII', '9º Ano EFII'),)
     ),
    ('Ensino Medio',(
    ('1-MED', '1º Ano Medio'),
    ('2-MED', '2º Ano Medio'),
    ('3-MED', '3º Ano Medio'),)
     ),
]


STRING_CHOICE = (
    ('A', 'Alfa'),
    ('B', 'Bravo'),
    ('C', 'Charlie'),
    ('D', 'Delta'),
)

TURNO_CHOICE = (
    ('M', 'Manha'),
    ('T', 'Tarde'),
    ('N', 'Noite'),
)

from .alunos_model import *
from .boletim_model import *
from .disciplinas_model import *
from .notas_model import *
from .professores_model import *
from .series_model import *
from .turmas_model import *
