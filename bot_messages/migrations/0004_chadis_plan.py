# Generated by Django 3.2.12 on 2022-03-13 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_messages', '0003_remove_message_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chadis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_kk', models.TextField(max_length=4096, null=True, verbose_name='хадис (каз)')),
                ('text_ru', models.TextField(max_length=4096, null=True, verbose_name='хадис (рус)')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='ramazan', verbose_name='Фото рамазана')),
                ('text', models.TextField(blank=True, max_length=500, verbose_name='Текст')),
                ('link', models.CharField(blank=True, max_length=1000, verbose_name='Ссылка на источник')),
            ],
            options={
                'verbose_name': 'План',
                'verbose_name_plural': 'План',
            },
        ),
    ]
