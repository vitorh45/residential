from django.db import models
from django.contrib.auth.models import AbstractUser
from localflavor.br.models import BRCPFField


class Resident(AbstractUser):
    cpf = BRCPFField('CPF')
    lot = models.CharField('Lote', max_length=20)

    class Meta:
        verbose_name = 'Resident'
        verbose_name_plural = 'Residents'