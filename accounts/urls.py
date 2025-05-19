from django.urls import path
from accounts.views import RegisterLoginView

app_name= 'accounts'

urlpatterns = [
    path('account/', RegisterLoginView.as_view(), name='register_login'),
]