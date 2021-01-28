# Generated by Django 2.2.12 on 2021-01-27 15:53

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('post_prob', '0014_auto_20210127_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.FloatField(default=52.01990374646353, null=True, verbose_name='Given this information, what is the probability that you outperformed 90% of the participants in the previous task?'),
        ),
    ]
