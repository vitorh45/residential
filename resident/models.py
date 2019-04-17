from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from localflavor.br.models import BRCPFField, BRPostalCodeField


class HouseResident(models.Model):
    name = models.CharField('Nome do morador', max_length=200, blank=True)
    birth_date = models.DateField('Data de nascimento', blank=True, default=datetime.now)
    resident = models.ForeignKey('Resident', on_delete=models.CASCADE)


class Resident(AbstractUser):
    cpf = BRCPFField('CPF', unique=True)
    birth_date = models.DateField('Data de nascimento', default=datetime.now)
    rg = models.CharField('RG', max_length=20, blank=True)

    # Address
    lot_block = models.CharField('Block do lote', max_length=20, blank=True, null=True)
    lot_number = models.IntegerField('Número do lote', blank=True, null=True)
    street = models.CharField('Rua/Av', max_length=250, blank=True)
    number = models.CharField('Número', max_length=10, blank=True)
    cep = BRPostalCodeField('Cep', blank=True)

    class Meta:
        verbose_name = 'Resident'
        verbose_name_plural = 'Residents'
