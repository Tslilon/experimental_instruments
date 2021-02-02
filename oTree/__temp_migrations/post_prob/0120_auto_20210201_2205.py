# Generated by Django 2.2.12 on 2021-02-02 06:05

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('post_prob', '0119_auto_20210201_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.FloatField(default=49.262207096539925, null=True, verbose_name='What is the probability that you ranked top 10%?'),
        ),
    ]
