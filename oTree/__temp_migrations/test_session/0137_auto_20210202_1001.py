# Generated by Django 2.2.12 on 2021-02-02 18:01

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('test_session', '0136_auto_20210202_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.IntegerField(default=23.30368918651875, null=True, verbose_name='What is the probability that you ranked top 10%?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='self_rating1',
            field=otree.db.models.IntegerField(default=2.2686003462324242, null=True, verbose_name="How well do you think you'll do in the task?"),
        ),
        migrations.AlterField(
            model_name='player',
            name='self_rating2',
            field=otree.db.models.IntegerField(default=5.240568686109723, null=True, verbose_name='How well do you think you did in the task?'),
        ),
    ]
