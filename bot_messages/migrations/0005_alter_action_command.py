# Generated by Django 3.2.12 on 2022-03-13 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_messages', '0004_chadis_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='command',
            field=models.IntegerField(blank=True, choices=[(0, 'Ораза кестесі'), (1, 'Қадір түні'), (2, 'Дұғалар'), (3, 'Сұрақ жауап (FAQ)'), (4, 'Ұсыныс, сын'), (5, 'Чатқа қосылу'), (6, 'Рамазан жоспары'), (7, 'Оқылу керек дұғалар'), (8, 'Сұрақ-жауап (қадір туні)'), (9, 'Қадір түні жайында'), (10, 'Қадір түнінде 10 сауапты іс'), (11, 'Қадір түнінде 10 күнәлі іс'), (12, 'Істелуі тиіс ең таңдаулы амалдар'), (13, 'Артқа'), (14, 'Хадистер'), (15, 'Рамазан күнделік')], verbose_name='Комманда'),
        ),
    ]
