# Generated by Django 2.2.12 on 2021-02-02 01:01

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('test_session', '0116_auto_20210201_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.IntegerField(default=38.61260631112322, null=True, verbose_name='What is the probability that you ranked top 10%?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='self_rating1',
            field=otree.db.models.IntegerField(default=7.246130899187076, null=True, verbose_name="How well do you think you'll do in the task?"),
        ),
        migrations.AlterField(
            model_name='player',
            name='self_rating2',
            field=otree.db.models.IntegerField(default=1.3080169617237258, null=True, verbose_name='How well do you think you did in the task?'),
        ),
    ]
