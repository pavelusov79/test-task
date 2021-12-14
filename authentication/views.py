from django.contrib.auth.views import LoginView, auth_login
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


class UserLoginView(LoginView):
    template_name = 'admin/login.html'

    def get_success_url(self):
        return reverse_lazy('main')

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        if form.get_user().is_superuser:
            return HttpResponseRedirect(reverse('admin:index'))
        return HttpResponseRedirect(self.get_success_url())


class SingUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('admin:login')
    template_name = 'main/register.html'
