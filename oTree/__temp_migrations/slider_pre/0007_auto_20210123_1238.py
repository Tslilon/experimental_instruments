# Generated by Django 2.2.12 on 2021-01-23 20:38

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('slider_pre', '0006_auto_20210123_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='rating',
        ),
        migrations.AddField(
            model_name='player',
            name='self_rating',
            field=otree.db.models.IntegerField(default=7.247952059723301, null=True, verbose_name="How well do you think you'll do? (1 = Very Badly, 10 = Very Well)"),
        ),
    ]
