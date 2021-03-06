# Generated by Django 2.2.12 on 2021-02-02 06:35

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('post_prob', '0122_auto_20210201_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.FloatField(default=16.911439005969765, null=True, verbose_name='What is the probability that you ranked top 10%?'),
        ),
    ]
