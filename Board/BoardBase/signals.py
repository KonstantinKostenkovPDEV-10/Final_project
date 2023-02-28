from django.core.mail import send_mail
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Response,Announcement
from .tasks import send_subscribers_change



@receiver(post_save, sender=Response)
def post_get(sender, instance,created, **kwargs):
    QuerySet_email = User.objects.filter(username=instance.user).values('email')
    announcement_email = list()
    announcement_email = QuerySet_email[0].get('email')
    QuerySet_announcement_id = Response.objects.filter(id=instance.id).values('announcement_id')
    announcement_user = Announcement.objects.filter(id=QuerySet_announcement_id[0].get('announcement_id')).values('user_id')
    announcement_user_id = announcement_user[0].get('user_id')
    QuerySet_response_email = User.objects.filter(id=announcement_user_id).values('email')
    response_email = list()
    response_email = QuerySet_response_email[0].get('email')
    url_title = f"http://127.0.0.1:8000/"
    if created:
        send_mail(
            subject=f'Получен новый отклик на ваше объявление на сайте фанатского MMORPG!',
            message=f'Получен новый отклик  от пользователя {instance.user} :{instance.response_text} ',
            from_email='admin008@mail.ru',
            recipient_list=[response_email],)
    else:
        send_mail(
            subject=f'Ваш отклик на объявление на сайте фанатского MMORPG был принят!',
            message=f'Ваш отклик принят на объявление {url_title}{instance.announcement_id}',
            from_email='admin008@mail.ru',
            recipient_list=[announcement_email], )




