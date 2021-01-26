# Generated by Django 2.2.12 on 2021-01-23 19:15

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0014_auto_20210123_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='rating',
            field=otree.db.models.IntegerField(default=2.709114804357732, null=True, verbose_name="How well do you think you'll do? (1 = Very Badly, 10 = Very Well)"),
        ),
    ]