from django.db import models
from django.contrib.auth.models import User


class ParkingPlaces(models.Model):
    name = models.CharField(max_length=32, verbose_name='парковочное место')
    img = models.ImageField(upload_to='media', blank=True)
    is_active = models.BooleanField(verbose_name='активное', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Парковочные места'


class Time(models.Model):
    parking = models.ForeignKey(ParkingPlaces, on_delete=models.CASCADE, related_name='time',
                                verbose_name='парковочное место')
    time_field = models.CharField(max_length=32, verbose_name='время для брони')

    def __str__(self):
        return self.time_field

    class Meta:
        verbose_name_plural = 'Время для бронирования парковочных мест'


class Reservation(models.Model):
    parking = models.ForeignKey(ParkingPlaces, on_delete=models.CASCADE, verbose_name='парковочное место')
    time = models.ForeignKey(Time, on_delete=models.CASCADE, verbose_name='время бронирования')
    date_field = models.DateField(verbose_name='дата для брони')
    employee = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='работник')

    class Meta:
        verbose_name_plural = 'Бронирование парковки'
