from django.db import models



class Rubric(models.Model):
    name = models.CharField(max_length=30, db_index=True,
                            verbose_name='Город')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Города'
        verbose_name = 'Город'
        ordering = ['name']


class Tt(models.Model):
    family = models.CharField(max_length=50, db_index=True,verbose_name='Фамилия')
    content = models.TextField(null=True, blank=True,verbose_name='Карточка абонента')
    nomer = models.CharField(max_length=12, null=True, blank=True, verbose_name='Номер телефона')
    rubric = models.ForeignKey('Rubric', null=True,
                               on_delete=models.PROTECT,
                               verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Абоненты'
        verbose_name = 'Абонент'
        ordering = ['family']


