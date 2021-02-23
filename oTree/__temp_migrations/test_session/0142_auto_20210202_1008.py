# Generated by Django 2.2.12 on 2021-02-02 18:08

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('test_session', '0141_auto_20210202_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.IntegerField(default=81.44585477151027, null=True, verbose_name='What is the probability that you ranked top 10%?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='self_rating1',
            field=otree.db.models.IntegerField(default=7.339291368490634, null=True, verbose_name="How well do you think you'll do in the task?"),
        ),
        migrations.AlterField(
            model_name='player',
            name='self_rating2',
            field=otree.db.models.IntegerField(default=8.938864007739548, null=True, verbose_name='How well do you think you did in the task?'),
        ),
    ]
