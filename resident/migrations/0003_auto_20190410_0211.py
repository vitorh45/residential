# Generated by Django 2.2 on 2019-04-10 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resident', '0002_auto_20190410_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resident',
            name='lot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lot.Lot'),
        ),
    ]
