from django.db import models
from secretaria.models.turmas_model import Turma
from phonenumber_field.modelfields import PhoneNumberField
from django_cpf_cnpj.fields import CPFField


class Aluno(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nome")
    sobrenome = models.CharField(max_length=150)
    # certidao = models.CharField(max_length=33, unique=True,
    #                             default='0000000000000', help_text="Número da certidão de nascimento")
    # mae = models.CharField(max_length=150, null=True, blank=True)
    # pai = models.CharField(max_length=150, null=True, blank=True)
    # cpf = CPFField(masked=True, null=True, blank=True, help_text="CPF do responsável financeiro")
    # tel1 = PhoneNumberField(null=True, blank=True, unique=True, help_text="Telefone da mãe")
    # tel2 = PhoneNumberField(null=True, blank=True, unique=True, help_text="Telefone do pai ou responsável financeiro")
    # endereco = models.CharField(max_length=250)
    # email = models.EmailField(max_length=200, help_text='email')
    # aluno = models.OneToOneField(Info, on_delete=models.CASCADE)
    classe = models.ForeignKey(Turma, null=True, blank=True,
                              on_delete=models.CASCADE, help_text="Turma que o aluno esta atualmente cursando")

    def __str__(self):
        return f'{self.name} {self.sobrenome}'

    class Meta:
        ordering = ('-name',)


class Info(models.Model):
    aluno = models.OneToOneField(Aluno, on_delete=models.CASCADE)
    certidao = models.CharField(max_length=33, unique=True,
                                default='0000000000000', help_text="Número da certidão de nascimento")
    mae = models.CharField(max_length=150, null=True, blank=True)
    pai = models.CharField(max_length=150, null=True, blank=True)
    cpf = CPFField(masked=True, null=True, blank=True, help_text="CPF do responsável financeiro")
    tel1 = PhoneNumberField(null=True, blank=True, unique=True, help_text="Telefone da mãe")
    tel2 = PhoneNumberField(null=True, blank=True, unique=True, help_text="Telefone do pai ou responsável financeiro")
    endereco = models.CharField(max_length=250)
    email = models.EmailField(max_length=200, help_text='email do responsável financeiro')
    # classe = models.ForeignKey(Turma, null=True, blank=True,
    #                            on_delete=models.CASCADE, help_text="Turma que o aluno esta atualmente cursando")

    def __str__(self):
        return f'{self.aluno}'

    class Meta:
        verbose_name = 'Dados Pessoais'
        verbose_name_plural = 'Informações Pessoais'