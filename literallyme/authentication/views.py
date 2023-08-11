from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.views.generic import CreateView

from .forms import *


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'authentication/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect('home')


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'authentication/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
