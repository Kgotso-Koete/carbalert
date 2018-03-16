# Generated by Django 2.0.3 on 2018-03-11 06:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('carbalert_django', '0003_thread_search_phrases'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchphrase',
            name='email_users',
            field=models.ManyToManyField(related_name='email_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='thread',
            name='text',
            field=models.TextField(max_length=1000),
        ),
    ]