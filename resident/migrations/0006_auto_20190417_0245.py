# Generated by Django 2.2 on 2019-04-17 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resident', '0005_auto_20190417_0238'),
    ]

    operations = [
        migrations.AddField(
            model_name='resident',
            name='lot_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Número do lote'),
        ),
        migrations.AlterField(
            model_name='resident',
            name='log_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Número do lote'),
        ),
    ]
