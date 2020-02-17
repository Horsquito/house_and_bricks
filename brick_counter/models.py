from django.db import models
from django.urls import reverse


class House(models.Model):
    address = models.CharField(max_length=100)
    year_of_construction = models.DateField()

    def get_absolute_url(self):
        return reverse('brick_counter:house_page', args=[self.pk])

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'
        ordering = ['year_of_construction']

    def __str__(self):
        return self.address


class Task(models.Model):
    number_of_bricks = models.PositiveIntegerField()
    date_and_time = models.DateTimeField()
    house = models.OneToOneField('House',
                                 null=True,
                                 blank=True,
                                 on_delete=models.CASCADE,
                                 verbose_name='Дом для закладки кирпичей')

    class Meta:
        verbose_name = 'Задание на закладку кирпичей'
        verbose_name_plural = 'Задания на закладку кирпичей'
        ordering = ['date_and_time']

    def __str__(self):
        return str(self.number_of_bricks)


