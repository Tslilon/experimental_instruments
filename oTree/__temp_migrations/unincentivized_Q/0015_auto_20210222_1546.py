# Generated by Django 2.2.12 on 2021-02-22 23:46

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('unincentivized_Q', '0014_auto_20210222_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='Q4',
            field=otree.db.models.FloatField(blank=True, default=42.48046971520208, null=True, verbose_name='Q4'),
        ),
        migrations.AlterField(
            model_name='player',
            name='gender',
            field=otree.db.models.IntegerField(blank=True, choices=[[1, 'Male'], [2, 'Female'], [3, 'Other, please speficify']], null=True, verbose_name='<strong>What is your gender?<\\strong>'),
        ),
    ]
