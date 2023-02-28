from ckeditor.widgets import CKEditorWidget
from django import forms
from ckeditor.fields import RichTextField
from django.forms import Textarea, CheckboxInput

from .models import Announcement, Response


class AnnouncementForm(forms.ModelForm):
    announcement_text = forms.CharField(widget=CKEditorWidget(),label='Текст объявления')
    header = forms.CharField(max_length=255, widget=Textarea(attrs={'cols': '40','rows':'1'}),label='Заголовок объявления')
    announcement_category = forms.CheckboxSelectMultiple()
    class Meta:
        model = Announcement
        fields = [
            'user',
            'header',
            'announcement_category',
            'announcement_text',
        ]



class ResponseForm(forms.ModelForm):
    response_text = forms.CharField(max_length=255, widget=Textarea(attrs={'cols': '40','rows':'3'}),label='Текст отклика')

    class Meta:
        model = Response
        fields = [
            'response_text',
               ]



class ModerationForm(forms.ModelForm):
    response_text = forms.CharField(max_length=255, widget=Textarea(attrs={'cols': '40','rows':'3'}),label='Текст отклика')
    class Meta:
        model = Response
        fields = [
            'user',
            'response_text',
            'activated',
        ]



