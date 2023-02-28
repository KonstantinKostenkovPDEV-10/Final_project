from random import random

import username as username
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import send_mail
from django.http import request
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.views.generic.edit import FormMixin, DeleteView, UpdateView

from .filter import AnnoucementFilter
from .forms import *
from .models import *

class CustomSuccessMessageMixin:
    @property
    def success_msg(self):
        return False
    def form_valid(self, form):
        messages.success(self.request,self.success_msg)
        return super().form_valid(form)
    def get_success_url(self):
        return '%s?id=%s' % (self.success_url,self.object().id)

class AnnouncementList(ListView):
    model = Announcement
    ordering = 'date_create'
    template_name = 'announcement_list.html'
    context_object_name = 'Announcement'
    paginate_by = 1
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = AnnoucementFilter(self.request.GET, queryset=self.get_queryset())
        return context

@method_decorator(login_required(login_url="/sign/login/"), name='dispatch')
class AnnouncementDetail(CustomSuccessMessageMixin,FormMixin,DetailView):
    template_name = 'announcement_detail.html'
    context_object_name = 'Announcement'
    form_class = ResponseForm
    queryset = Announcement.objects.all()
    success_msg = 'Отклик на данное объявление успешно добавлен!'
    success_url = '/announcement/'

    def get_success_url(self,**kwargs):
        return reverse('announcement_detail',kwargs={'pk':self.get_object().id})

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.announcement= self.get_object()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

    def post(self,request,*args,**kwargs):
        form = self.get_form()
        if form.is_valid():
            #print(self.get_object().id)
            #print('111')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

@method_decorator(login_required(login_url="/sign/login/"), name='dispatch')
class AnnouncementCreateView(CreateView):
    model = Announcement
    template_name = 'announcement_create.html'
    #permission_required= ('Announcement.add_post',)
    form_class = AnnouncementForm
    success_url = '/'


@method_decorator(login_required(login_url="/sign/login/"), name='dispatch')
class AnnouncementDeleteView(DeleteView):
    template_name = 'announcement_delete.html'
    queryset = Announcement.objects.all()
    success_url = '/'
    #permission_required = ('News.delete_post', )

@method_decorator(login_required(login_url="/sign/login/"), name='dispatch')
class AnnouncementUpdateView(UpdateView):
    template_name = 'announcement_create.html'
    #permission_required = ('News.change_post',)
    form_class = AnnouncementForm
    success_url = '/'
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Announcement.objects.get(pk=id)

@method_decorator(login_required(login_url="/sign/login/"), name='dispatch')
class UserProfileView(ListView):
    model = Response
    ordering = 'date_create'
    template_name = 'userprofile.html'
    #context_object_name = 'Announcement'
    paginate_by = 1

    def get(self, request):
        username = request.user
        announcement_user= Announcement.objects.filter(user_id=User.objects.filter(username=username).first().id)
        bound_form = ModerationForm
        return render(request, 'userprofile.html', context={'form': bound_form, 'announcement_user': announcement_user,})


    def post(self, request, *args, **kwargs):
        bound_form = ResponseForm
        QuerySet = request.POST.getlist('boxes')

        for res in QuerySet:
            context = Response.objects.filter(announcement_id=res)
            return render(request, 'userprofile.html', context={'form': bound_form, 'context': context})

@method_decorator(login_required(login_url="/sign/login/"), name='dispatch')
class ModerationView(TemplateView):
    model = Response
    ordering = 'date_create'
    template_name = 'userprofile.html'
    #context_object_name = 'Announcement'
    paginate_by = 1

@method_decorator(login_required(login_url="/sign/login/"), name='dispatch')
class ModerationDeleteView(DeleteView):
    template_name = 'moderation_delete.html'
    queryset = Response.objects.all()
    success_url = '/userprofile/'
    #permission_required = ('News.delete_post', )

@method_decorator(login_required(login_url="/sign/login/"), name='dispatch')
class ModerationUpdateView(UpdateView):
    template_name = 'moderation_update.html'
    #permission_required = ('News.change_post',)
    form_class = ModerationForm
    success_url = '/userprofile'
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Response.objects.get(pk=id)






