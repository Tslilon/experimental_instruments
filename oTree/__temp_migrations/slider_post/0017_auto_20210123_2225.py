# Generated by Django 2.2.12 on 2021-01-24 06:25

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('slider_post', '0016_auto_20210123_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='self_rating',
            field=otree.db.models.IntegerField(default=9.927078814826208, null=True, verbose_name='How well do you think you did in the task? (0 = Very Badly, 10 = Very Well)'),
        ),
    ]
