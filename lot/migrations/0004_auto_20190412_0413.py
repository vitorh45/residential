# Generated by Django 2.2 on 2019-04-12 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lot', '0003_auto_20190412_0413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lot',
            name='number',
            field=models.IntegerField(verbose_name='Número do lote'),
        ),
    ]
