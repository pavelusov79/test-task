import datetime
from django import forms

from main.models import Reservation, Time


class DateInput(forms.DateInput):
    input_type = 'date'


class ReservationForm(forms.ModelForm):
    class Meta:
        class DateInput(forms.DateInput):
            input_type = 'date'

        model = Reservation
        fields = ['date_field', 'time']

        widgets = {
            'date_field': DateInput(),
        }

        labels = {
            'date_field': 'Выберите дату на которую хотите забронировать',
        }

    def __init__(self, *args, **kwargs):
        pk = kwargs.pop('pk')
        print('data = ', kwargs)
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['time'].queryset = Time.objects.filter(parking__id=pk)

    def clean(self):
        cleaned_data = super(ReservationForm, self).clean()
        date_field = cleaned_data.get('date_field')
        time_field = cleaned_data.get('time')
        if date_field:
            res = date_field - datetime.date.today()
            delta = datetime.timedelta(days=2)
            if date_field < datetime.date.today():
                raise forms.ValidationError({'date_field': 'Выбранная вами дата не может быть раньше текущей'})
            if res > delta:
                raise forms.ValidationError({'date_field': 'Эллектронная запись доступна только в пределах двух дней.'})
        if date_field and time_field:
            if date_field == datetime.date.today():
                print('str(time)= ', str(time_field).split('-')[0])
                if str(time_field).split('-')[0] < datetime.datetime.now().strftime('%H:%M'):
                    raise forms.ValidationError({'time': 'Час на которой вы планируете забронировать уже прошел. '
                                                               'Пожалуйста выберите час записи больше текущего.'})
        return cleaned_data