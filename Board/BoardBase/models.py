from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField



class Category(models.Model):
    category_name = models.CharField(max_length=128)
    def __str__(self):
        return f'{self.category_name}'

class Announcement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    announcement_text = RichTextUploadingField()
    date_create = models.DateField(auto_now_add=True)
    header = models.CharField(max_length=255)
    announcement_category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Response(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    response_text = models.TextField()
    date_create = models.DateField(auto_now_add=True)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE,related_name='announcement_response')
    activated = models.BooleanField(default=False)
    def get_subscribers_emails(self):
        QuerySubs = Response.objects.filter(announcement_id=self).values('user_id')
        QuerySet_email = User.objects.filter(id__in=QuerySubs).values('email')
        _emails = list()
        for qs in QuerySet_email:
            emails = qs.get('email')
            _emails.append(emails)
        return _emails
