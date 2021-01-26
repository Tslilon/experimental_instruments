# Generated by Django 2.2.12 on 2021-01-23 20:52

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('slider_pre', '0014_auto_20210123_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='self_rating',
            field=otree.db.models.IntegerField(default=5.1431993957363975, null=True, verbose_name="How well do you think you'll do in the task? (1 = Very Badly, 10 = Very Well)"),
        ),
    ]
