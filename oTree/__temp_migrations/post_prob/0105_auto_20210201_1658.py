# Generated by Django 2.2.12 on 2021-02-02 00:58

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('post_prob', '0104_auto_20210201_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.FloatField(default=21.672720670353883, null=True, verbose_name='What is the probability that you ranked top 10%?'),
        ),
    ]
