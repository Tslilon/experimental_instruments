# Generated by Django 2.2.12 on 2021-01-24 06:21

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('slider_pre', '0026_auto_20210123_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='self_rating',
            field=otree.db.models.IntegerField(default=7.231685875595066, null=True, verbose_name="How well do you think you'll do in the task? (0 = Very Badly, 10 = Very Well)"),
        ),
    ]
