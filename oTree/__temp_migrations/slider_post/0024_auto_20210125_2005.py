# Generated by Django 2.2.12 on 2021-01-26 04:05

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('slider_post', '0023_auto_20210125_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='self_rating',
            field=otree.db.models.IntegerField(default=5.362034224253113, null=True, verbose_name='How well do you think you did in the task?'),
        ),
    ]
