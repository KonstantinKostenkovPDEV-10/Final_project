
from django.urls import path, include,reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView,TemplateView
from .views import BaseRegisterView,GetCodeView




urlpatterns =   [
    path('login/',LoginView.as_view(template_name='sign/login.html'),name='login'),
    path('logout/', LogoutView.as_view(template_name='sign/logout.html'), name='logout'),
    path('signup/',BaseRegisterView.as_view(template_name='sign/signup.html'),name='signup'),
    path('code/', GetCodeView.as_view(template_name='code.html'), name='code'),
    path('accounts/', include('allauth.urls')),
]
