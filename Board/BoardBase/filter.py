from django.forms import forms, Textarea,models
from django_filters import FilterSet
from .models import Announcement


class AnnoucementFilter(FilterSet):
    class Meta:
        model = Announcement
        fields = ('header', 'date_create', )
        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs['class']='input-label'
                self.fields['header'].widget = Textarea(attrs={'cols':40,'rows':1})
                self.fields['header'].label = 'Заголовок объявления'
