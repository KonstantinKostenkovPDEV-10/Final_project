from allauth.account.forms import UserForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .forms import BaseRegisterForm
from .models import *
from django.shortcuts import redirect, render
import random
from django.core.mail import send_mail, EmailMultiAlternatives
from django.http import HttpResponse



class BaseRegisterView(CreateView):
    model = User
    template_name = 'sign/signup.html'
    form_class = BaseRegisterForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BaseRegisterForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            active = form.save(commit=False)
            active.is_active = False
            active.save()
            request.session['user'] = form.cleaned_data['username']
            request.session['email'] = form.cleaned_data['email']
        else:
            return HttpResponse("404")

        return redirect('/sign/code/', request.POST['username'])

class GetCodeView(TemplateView):
    template_name = 'sign/code.html'


    def get(self,request):
        code=random.randint(100000, 999999)
        request.session['code'] = code

        email_session = request.session.get('email')
        request.session.modified = True
        code_session = request.session.get('code')
        send_mail(
            subject=f'Завершите регистрацию на фанатском сайте  MMORPG!',
            message=f'Код активации ' + str(code_session),
            from_email='admin008@mail.ru',
            recipient_list=[email_session],
        )
        activation = 0
        return render(request, 'code.html', {'activation': activation})

    def post(self, request, *args, **kwargs):
        code_form = request.POST.get('code')
        code_session = request.session.get('code')
        user_session = request.session.get('user')
        if int(code_form) - int(code_session) == 0:
            User.objects.filter(username=user_session).update(is_active=True)
            print("коды совпали")
            activation = 10
            redirect('/sign/login/')
        else:
            activation = 1

        return render(request, 'code.html', {'activation': activation})









