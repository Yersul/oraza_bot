# Generated by Django 3.2.12 on 2022-02-28 20:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot_messages', '0012_alter_message_actions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pray',
            name='text_kk',
        ),
        migrations.RemoveField(
            model_name='pray',
            name='text_ru',
        ),
    ]