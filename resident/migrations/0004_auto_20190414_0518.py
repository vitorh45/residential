# Generated by Django 2.2 on 2019-04-14 05:18

from django.db import migrations
from resident.models import BRCPFField


class Migration(migrations.Migration):

    dependencies = [
        ('resident', '0003_auto_20190410_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='cpf',
            field=BRCPFField(max_length=14, unique=True, verbose_name='CPF'),
        ),
    ]
