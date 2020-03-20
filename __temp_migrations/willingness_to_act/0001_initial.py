# Generated by Django 2.2.4 on 2020-03-20 12:08

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='willingness_to_act_group', to='otree.Session')),
            ],
            options={
                'db_table': 'willingness_to_act_group',
            },
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='willingness_to_act_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'willingness_to_act_subsession',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_gbat_arrived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('forego_future', otree.db.models.StringField(choices=[['0', ''], ['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', ''], ['8', ''], ['9', ''], ['10', '']], max_length=10000, null=True, verbose_name='\n        How willing are you to give up something that is beneficial for you today \n        in order to benefit more from that in the future?\n        ')),
                ('punish_unfair', otree.db.models.StringField(choices=[['0', ''], ['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', ''], ['8', ''], ['9', ''], ['10', '']], max_length=10000, null=True, verbose_name='\n        How willing are you to punish someone who treats you unfairly, \n        even if there may be costs for you? \n        ')),
                ('punish_unfair_others', otree.db.models.StringField(choices=[['0', ''], ['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', ''], ['8', ''], ['9', ''], ['10', '']], max_length=10000, null=True, verbose_name='\n        How willing are you to punish someone who treats others unfairly, \n        even if there may be costs for you? \n        ')),
                ('give_free', otree.db.models.StringField(choices=[['0', ''], ['1', ''], ['2', ''], ['3', ''], ['4', ''], ['5', ''], ['6', ''], ['7', ''], ['8', ''], ['9', ''], ['10', '']], max_length=10000, null=True, verbose_name='\n        How willing are you to give to good causes without expecting anything in return?\n        ')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='willingness_to_act.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='willingness_to_act_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='willingness_to_act_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='willingness_to_act.Subsession')),
            ],
            options={
                'db_table': 'willingness_to_act_player',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='willingness_to_act.Subsession'),
        ),
    ]
