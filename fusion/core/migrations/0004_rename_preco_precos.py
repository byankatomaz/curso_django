# Generated by Django 4.2.7 on 2023-11-09 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_cliente_planos_preco'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Preco',
            new_name='Precos',
        ),
    ]
