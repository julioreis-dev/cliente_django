from django.contrib import admin
from secretaria.models.boletim_model import Boletim
from secretaria.models.series_model import Serie
from secretaria.models.turmas_model import Turma
from secretaria.models.disciplinas_model import Materia
from secretaria.models.professores_model import Professor
from secretaria.models.notas_model import Nota
from secretaria.models.alunos_model import Aluno, Info


class NotaInline(admin.TabularInline):
    model = Nota
    extra = 0


class AlunoInline(admin.TabularInline):
    model = Aluno
    extra = 0


class InfoInline(admin.StackedInline):
    model = Info
    extra = 0


class SerieAdmin(admin.ModelAdmin):
    list_display = ('id', 'ensino')


class TurmaAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados da turma', {'fields': ('serie', 'classe', 'turno', 'ano')}),
        ('Designação de professores', {'fields': ('prof',)}),
    )
    list_display = ('serie', 'classe', 'turno', 'ano')
    filter_horizontal = ('prof',)
    inlines = (AlunoInline,)
    search_fields = ['serie__ensino', 'classe', 'turno', 'ano']
    raw_id_fields = ('serie',)


class ProfessorAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados Pessoais', {'fields': ('name', 'sobrenome', 'admissao')}),
        ('Disciplinas Ministradas', {'fields': ('disciplina',)}),
    )
    list_display = ('name', 'sobrenome')
    readonly_fields = ('admissao',)
    filter_horizontal = ('disciplina',)


class AlunoAdmin(admin.ModelAdmin):
    list_display = ('name', 'sobrenome', 'classe')
    raw_id_fields = ('classe',)
    search_fields = ('name', 'sobrenome', 'info__cpf', 'classe__serie__ensino')
    inlines = (InfoInline,)


class InfoAdmin(admin.ModelAdmin):
    list_display = ('aluno',)
    search_fields = ('name', 'certidao', 'cpf')
    # raw_id_fields = ('turma', )
    # inlines = (NotaInline,)


class NotaAdmin(admin.ModelAdmin):
    list_display = ('boletim', 'media',)
    # raw_id_fields = ('aluno',)
    # search_fields = ['aluno', 'turma']


class BoletimAdmin(admin.ModelAdmin):
    raw_id_fields = ('aluno', 'turma')
    inlines = (NotaInline,)
    search_fields = ('aluno__name', 'aluno__sobrenome', 'aluno__info__certidao',
                     'aluno__info__cpf', 'turma__ano', 'turma__serie__ensino')


admin.site.register(Materia)
admin.site.register(Serie, SerieAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Boletim, BoletimAdmin)
# admin.site.register(Info, InfoAdmin)
# admin.site.register(Nota, NotaAdmin)
