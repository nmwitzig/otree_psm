# Generated by Django 2.2.4 on 2020-03-20 13:35

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('self_assessment', '0002_player_risk_assessment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='risk_assessment',
            field=otree.db.models.StringField(choices=[['0', ''], ['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', ''], ['8', ''], ['9', ''], ['10', '']], max_length=10000, null=True, verbose_name='\n            In general, how willing or unwilling are you to take risks?\n            '),
        ),
    ]
