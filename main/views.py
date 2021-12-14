from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from main.models import ParkingPlaces, Reservation, Time
from main.forms import ReservationForm


class PlacesListView(ListView):
    model = ParkingPlaces
    template_name = 'main/index.html'
    paginate_by = 12


class ReservationCreateView(LoginRequiredMixin, CreateView):
    template_name = 'main/reservation.html'
    form_class = ReservationForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['place'] = ParkingPlaces.objects.get(id=self.kwargs['pk'])
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['pk'] = self.kwargs['pk']
        return kwargs

    def form_valid(self, form):
        ctx = self.get_context_data()
        obj = form.save(commit=False)
        obj.parking = ctx['place']
        obj.employee = self.request.user
        obj.save()
        return super().form_valid(form)


class EmployeeReservationListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        return Reservation.objects.filter(employee=self.request.user)


def load_time(request):
    date = request.GET.get('date')
    parking = request.GET.get('parking')

    time_set = Time.objects.filter(parking=int(parking.split('#')[-1]))
    time_busy = []
    if date:
        query = Reservation.objects.filter(date_field=date, parking=int(parking.split('#')[-1]))
        for item in query:
            time_busy.append(str(item.time))
    return render(request, 'main/time_choice_list.html', {'time_set': time_set, 'time_busy': time_busy})