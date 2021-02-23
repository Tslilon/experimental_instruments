# Generated by Django 2.2.12 on 2021-01-30 21:02

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('post_prob', '0025_auto_20210130_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.FloatField(default=81.0169813702244, null=True, verbose_name='Given this information, what is the probability that you outperformed 90% of the participants in the previous task?'),
        ),
    ]
