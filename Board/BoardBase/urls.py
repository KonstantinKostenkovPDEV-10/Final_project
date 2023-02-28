from django.contrib import admin
from django.urls import path, include
from .views import *
from .views import ModerationView

urlpatterns = [
    path('', AnnouncementList.as_view()),
    path('<int:pk>', AnnouncementDetail.as_view(), name='announcement_detail'),
    path('create/', AnnouncementCreateView.as_view(), name='announcement_create'),
    path('delete/<int:pk>', AnnouncementDeleteView.as_view(), name='announcement_delete'),
    path('update/<int:pk>', AnnouncementUpdateView.as_view(), name='announcement_update'),
    path('userprofile/',UserProfileView.as_view(),name='userprofile'),
    path('moderation/delete/<int:pk>',ModerationDeleteView.as_view(template_name='moderation_delete.html'),name='moderation_delete'),
    path('moderation/update/<int:pk>', ModerationUpdateView.as_view(template_name='moderation_update.html'), name='moderation_update'),
]
