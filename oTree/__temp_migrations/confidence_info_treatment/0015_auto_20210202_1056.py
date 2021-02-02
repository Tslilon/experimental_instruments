# Generated by Django 2.2.12 on 2021-02-02 18:56

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('confidence_info_treatment', '0014_auto_20210202_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.FloatField(default=48.76375844541019, null=True, verbose_name='What is the probability that you ranked top 10%?'),
        ),
    ]
