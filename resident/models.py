from django.db import models
from django.contrib.auth.models import AbstractUser
from localflavor.br.models import BRCPFField, BRPostalCodeField
from datetime import datetime
from lot.models import Lot


class HouseResident(models.Model):
    name = models.CharField('Nome do morador', max_length=200, blank=True)
    birth_date = models.DateField('Data de nascimento', blank=True, default=datetime.now)
    resident = models.ForeignKey('Resident', on_delete=models.CASCADE)


class Resident(AbstractUser):

    cpf = BRCPFField('CPF', unique=True)
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE, blank=True, null=True)
    birth_date = models.DateField('Data de nascimento', default=datetime.now)

    rg = models.CharField('RG', max_length=20, blank=True)

    # Address
    street = models.CharField('Rua/Av', max_length=250, blank=True)
    number = models.CharField('Número', max_length=10, blank=True)
    cep = BRPostalCodeField('Cep', blank=True)

    class Meta:
        verbose_name = 'Resident'
        verbose_name_plural = 'Residents'
