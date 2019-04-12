from django.db import models


class Lot(models.Model):

    block = models.CharField('Bloco', max_length=3)
    number = models.IntegerField('Número do lote')

    def __str__(self):
        return f'Lote: {self.block}{self.number}'

    class Meta:
        verbose_name = 'Lote'
        verbose_name_plural = 'Lotes'
