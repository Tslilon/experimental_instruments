# Generated by Django 2.2.12 on 2021-02-02 18:04

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('unincentivized_Q', '0011_auto_20210202_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='Q4',
            field=otree.db.models.FloatField(blank=True, default=50.977216755152796, null=True, verbose_name='Q4'),
        ),
    ]
