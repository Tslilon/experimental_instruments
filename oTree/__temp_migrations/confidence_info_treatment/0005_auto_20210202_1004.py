# Generated by Django 2.2.12 on 2021-02-02 18:04

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('confidence_info_treatment', '0004_auto_20210202_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.FloatField(default=20.459884808869276, null=True, verbose_name='What is the probability that you ranked top 10%?'),
        ),
    ]
