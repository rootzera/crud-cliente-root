# Generated by Django 3.1.4 on 2020-12-31 01:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_cliente_rg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='rg',
        ),
    ]