# Generated by Django 2.2.12 on 2021-02-01 21:30

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('post_prob', '0097_auto_20210201_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.FloatField(default=22.944322879762534, null=True, verbose_name='What is the probability that you outperformed 90% of the participants in the previous task?'),
        ),
    ]
