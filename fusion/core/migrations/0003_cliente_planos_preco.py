# Generated by Django 4.2.7 on 2023-11-09 11:39

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_recursos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('profissao', models.CharField(max_length=100, verbose_name='Profissão')),
                ('opiniao', models.TextField(max_length=200, verbose_name='Opinião')),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, upload_to='equipe', variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Planos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('plano', models.CharField(max_length=100, verbose_name='Plano')),
            ],
            options={
                'verbose_name': 'Plano',
                'verbose_name_plural': 'Planos',
            },
        ),
        migrations.CreateModel(
            name='Preco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=100, verbose_name='Recurso')),
                ('descricao', models.TextField(max_length=200, verbose_name='Descrição')),
                ('icone', models.CharField(choices=[('lni-package', 'Caixa'), ('lni-drop', 'Gota'), ('lni-star', 'Estrela')], max_length=16, verbose_name='Icone')),
                ('plano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.planos', verbose_name='Plano')),
            ],
            options={
                'verbose_name': 'Preço',
                'verbose_name_plural': 'Preços',
            },
        ),
    ]