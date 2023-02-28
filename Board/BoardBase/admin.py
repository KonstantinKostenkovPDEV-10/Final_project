from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Category, Response, Announcement
from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget





class AnnouncementAdminForm(forms.ModelForm):
    announcement_text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Announcement
        fields = '__all__'




class AnnouncementAdmin(admin.ModelAdmin):
    form = AnnouncementAdminForm

admin.site.register(Announcement, AnnouncementAdmin)
admin.site.register(Category)
admin.site.register(Response)