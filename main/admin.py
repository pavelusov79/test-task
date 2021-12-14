from django.contrib import admin
from main.models import ParkingPlaces, Time, Reservation


admin.site.register(ParkingPlaces)


@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ('parking', 'time_field')
    list_filter = ('parking',)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date_field', 'time', 'parking')
    list_filter = ('parking', 'date_field', 'employee')

