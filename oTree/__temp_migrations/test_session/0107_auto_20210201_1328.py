# Generated by Django 2.2.12 on 2021-02-01 21:28

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('test_session', '0106_auto_20210201_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.IntegerField(default=86.25920732194737, null=True, verbose_name='What is the probability that you outperformed 90% of the participants in the previous task?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='self_rating1',
            field=otree.db.models.IntegerField(default=1.8247130126607691, null=True, verbose_name="How well do you think you'll do in the task?"),
        ),
        migrations.AlterField(
            model_name='player',
            name='self_rating2',
            field=otree.db.models.IntegerField(default=9.35389099870338, null=True, verbose_name='How well do you think you did in the task?'),
        ),
    ]
