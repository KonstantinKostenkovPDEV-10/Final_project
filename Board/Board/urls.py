
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('BoardBase.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('sign/', include('sign.urls')),


]
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        }),
    ]



