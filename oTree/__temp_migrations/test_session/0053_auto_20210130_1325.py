# Generated by Django 2.2.12 on 2021-01-30 21:25

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('test_session', '0052_auto_20210130_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.IntegerField(default=19.50805049015958, null=True, verbose_name='What is the probability that you outperformed 90% of the participants in the previous task?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='self_rating1',
            field=otree.db.models.IntegerField(default=4.40301335129801, null=True, verbose_name="How well do you think you'll do in the task?"),
        ),
        migrations.AlterField(
            model_name='player',
            name='self_rating2',
            field=otree.db.models.IntegerField(default=8.153179054309469, null=True, verbose_name='How well do you think you did in the task?'),
        ),
    ]
