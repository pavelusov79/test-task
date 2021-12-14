from django.urls import path
from django.contrib.auth.views import LogoutView
from authentication import views

app_name = 'authentication'


urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.SingUpView.as_view(), name='register')
]