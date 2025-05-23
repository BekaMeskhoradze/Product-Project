from django.urls import reverse_lazy
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView

class RegisterLoginView(View):
    template_name = 'register_login.html'

    def get(self, request):
        register_form = CustomUserCreationForm()
        login_form = AuthenticationForm()
        return render(request, self.template_name, {
            'register_form': register_form,
            'login_form': login_form,
        })

    def post(self, request):
        if 'register' in request.POST:
            request.session['register_data'] = request.POST
            return redirect('accounts:register_login')

        elif 'login' in request.POST:
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('core:index')
            else:
                messages.error(request, "Invalid username or password.")
                return redirect('accounts:register_login')

        return redirect('accounts:register_login')

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET' and 'register_data' in request.session:
            post_data = request.session.pop('register_data')
            register_form = CustomUserCreationForm(post_data)
            login_form = AuthenticationForm()
            if register_form.is_valid():
                register_form.save()
                return redirect('accounts:register_login')
            else:
                messages.error(request, "Please correct the errors below.")
                return render(request, self.template_name, {
                    'register_form': register_form,
                    'login_form': login_form,
                    'show_register': True,
                })
        return super().dispatch(request, *args, **kwargs)

