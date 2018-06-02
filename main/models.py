from django.db import models

__all__ = ('Number', )

class Number(models.Model):
    number_1 = models.DecimalField('Número 1', max_digits=5, decimal_places=2)
    number_2 = models.DecimalField('Numero 2', max_digits=5, decimal_places=2)
    number_3 = models.DecimalField('Número 3', max_digits=5, decimal_places=2)
    number_4 = models.DecimalField('Número 4', max_digits=5, decimal_places=2)
    
    def __str__(self):
        return '1st: {}, 2nd: {}, 3th: {}, 4th: {}'.format(
            self.number_1,
            self.number_2,
            self.number_3,
            self.number_4
        )

    class Meta:
        verbose_name = 'Number'
        verbose_name_plural = 'Numbers'