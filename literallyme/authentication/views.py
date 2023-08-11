from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.views.generic import CreateView

from mainapp.utils import DataMixin
from .forms import *


class RegisterUserView(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'authentication/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title='Registration')

        return dict(list(context.items()) + list(mixin_context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect('home')


class LoginUserView(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'authentication/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title='Login')

        return dict(list(context.items()) + list(mixin_context.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
