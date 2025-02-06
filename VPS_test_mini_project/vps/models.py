from django.db import models
from .enums import VPSStatus


class VPS(models.Model):
    '''Модель для представления сервера.'''

    uid = models.AutoField(primary_key=True)
    cpu = models.PositiveIntegerField(
        verbose_name='CPU (Количество ядер)'
    )
    ram = models.PositiveIntegerField(
        verbose_name='RAM (Мб)',
    )
    hdd = models.PositiveIntegerField(
        verbose_name='Объём диска (ГБ)',
    )
    status = models.CharField(
        max_length=15,
        choices=VPSStatus.choices(),
        default=VPSStatus.STOPPED.value,
        verbose_name='Статус',
    )

    class Meta:
        verbose_name = 'VPS'
        verbose_name_plural = 'VPS'
        ordering = ('uid',)
        constraints = (
            models.CheckConstraint(
                check=models.Q(ram__gte=1024),
                name='ram_minimum'
            ),
        )

    def __str__(self):
        return f'VPS: идентификатор - {self.uid}, статус - {self.status}'
