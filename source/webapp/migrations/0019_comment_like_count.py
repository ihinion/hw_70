# Generated by Django 2.2.13 on 2020-10-12 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0018_commentlike'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='like_count',
            field=models.IntegerField(default=0, verbose_name='Счетчик лайков'),
        ),
    ]
