# Generated by Django 3.2.17 on 2023-02-19 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BoardBase', '0005_response_activated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='activated',
            field=models.BooleanField(default=False),
        ),
    ]
