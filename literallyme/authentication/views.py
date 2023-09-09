from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import RegisterUserForm, LoginUserForm, UpdateUserForm, CustomProfileForm
from .models import CustomProfile

from mainapp.utils import *


class RegisterUserView(CreateView):
    form_class = RegisterUserForm
    template_name = 'authentication/auth/register.html'

    def form_valid(self, form):
        user = form.save()
        # that pic is in base dir media dir
        CustomProfile.objects.create(user=user, profile_pic='/authentication/img/default_profile_pic.jpg')
        login(self.request, user)

        return redirect('home')


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'authentication/auth/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class ProfilePageView(DataMixin, LoginRequiredMixin, DetailView):
    model = User
    template_name = 'authentication/user/profile_page.html'
    context_object_name = 'user_info'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title=f'User {self.object.username}')

        return dict(list(context.items()) + list(mixin_context.items()))


@login_required(login_url='home')
def update_user_view(request, username):
    current_user = User.objects.get(username=request.user.username)
    form = UpdateUserForm(request.POST or None, instance=current_user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('profile_page', username=request.POST['username'])

    context = {
        'title': f'Update {current_user.username}\'s info',
        'form': form
    }

    return render(request, 'authentication/user/update_user.html', context=context)


class UserDeleteView(DataMixin, LoginRequiredMixin, DeleteView):
    model = User
    context_object_name = 'current_user'
    template_name = 'authentication/user/delete_user.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title=f'Delete account {self.object.username}')

        return dict(list(context.items()) + list(mixin_context.items()))


class ChangeProfilePicView(DataMixin, LoginRequiredMixin, UpdateView):
    model = CustomProfile
    form_class = CustomProfileForm
    template_name = 'authentication/custom_profile/change_profile_pic.html'
    context_object_name = 'form'
    login_url = reverse_lazy('home')
    pk_url_kwarg = 'user_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mixin_context = self.get_user_context(title='Change profile pic')

        return dict(list(context.items()) + list(mixin_context.items()))

    def get_success_url(self):
        return reverse_lazy('profile_page', kwargs={'username': self.object.user.username})
