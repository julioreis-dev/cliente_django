# Generated by Django 3.2.7 on 2021-09-29 15:50

from django.db import migrations, models
import django.db.models.deletion
import django_cpf_cnpj.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0002_auto_20210928_1620'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aluno',
            options={'ordering': ('-name',)},
        ),
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=django_cpf_cnpj.fields.CPFField(blank=True, help_text='CPF do responsável financeiro', max_length=14, null=True),
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certidao', models.CharField(default='0000000000000', help_text='Número da certidão de nascimento', max_length=33, unique=True)),
                ('mae', models.CharField(blank=True, max_length=150, null=True)),
                ('pai', models.CharField(blank=True, max_length=150, null=True)),
                ('cpf', django_cpf_cnpj.fields.CPFField(blank=True, help_text='CPF do responsável financeiro', max_length=14, null=True)),
                ('tel1', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Telefone da mãe', max_length=128, null=True, region=None, unique=True)),
                ('tel2', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Telefone do pai ou responsável financeiro', max_length=128, null=True, region=None, unique=True)),
                ('endereco', models.CharField(max_length=250)),
                ('email', models.EmailField(help_text='email', max_length=200)),
                ('aluno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='secretaria.aluno')),
                ('classe', models.ForeignKey(blank=True, help_text='Turma que o aluno esta atualmente cursando', null=True, on_delete=django.db.models.deletion.CASCADE, to='secretaria.turma')),
            ],
        ),
    ]