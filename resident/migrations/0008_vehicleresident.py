# Generated by Django 2.2 on 2019-04-30 03:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resident', '0007_remove_resident_log_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleResident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(blank=True, max_length=50, verbose_name='Modelo')),
                ('brand', models.CharField(blank=True, max_length=50, verbose_name='Marca')),
                ('color', models.CharField(blank=True, max_length=30, verbose_name='Cor')),
                ('plate', models.CharField(blank=True, max_length=7, verbose_name='Placa')),
                ('year', models.IntegerField(blank=True, verbose_name='Ano de fabricação')),
                ('resident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]