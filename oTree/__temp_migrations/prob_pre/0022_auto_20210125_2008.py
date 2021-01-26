# Generated by Django 2.2.12 on 2021-01-26 04:08

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('prob_pre', '0021_auto_20210125_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='probability',
            field=otree.db.models.FloatField(default=0.09350031705286121, null=True, verbose_name='What is the probability that you outperformed 90% of the participants in the previous task?'),
        ),
    ]