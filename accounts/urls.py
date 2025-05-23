from django.urls import path, reverse_lazy
from accounts.views import RegisterLoginView
from django.contrib.auth.views import LogoutView

app_name= 'accounts'

urlpatterns = [
    path('account/', RegisterLoginView.as_view(), name='register_login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('accounts:register_login')), name='logout')
]