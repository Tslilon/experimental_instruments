# Generated by Django 2.2.12 on 2021-01-31 19:28

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('test_session', '0073_auto_20210131_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.IntegerField(default=90.74787796240373, null=True, verbose_name='What is the probability that you outperformed 90% of the participants in the previous task?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='self_rating1',
            field=otree.db.models.IntegerField(default=1.1708886171915822, null=True, verbose_name="How well do you think you'll do in the task?"),
        ),
        migrations.AlterField(
            model_name='player',
            name='self_rating2',
            field=otree.db.models.IntegerField(default=9.733366639692415, null=True, verbose_name='How well do you think you did in the task?'),
        ),
    ]
