# Generated by Django 3.1.3 on 2020-11-11 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notify', '0005_auto_20201105_0650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slackuser',
            name='sync_message',
        ),
        migrations.RemoveField(
            model_name='slackuser',
            name='sync_status',
        ),
        migrations.RemoveField(
            model_name='slackuser',
            name='synqued_at',
        ),
        migrations.RemoveField(
            model_name='slackuser',
            name='team',
        ),
        migrations.AlterField(
            model_name='slackteam',
            name='owner',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='SlackUserTeam',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('sync_status',
                 models.CharField(choices=[('INCOMPLETED', 'Incompleted'),
                                           ('COMPLETED', 'Completed')],
                                  default='INCOMPLETED',
                                  max_length=15)),
                ('sync_message',
                 models.CharField(
                     blank=True,
                     default=None,
                     help_text=
                     'Contains any success or error messages depending on the status',
                     max_length=100,
                     null=True)),
                ('synqued_at',
                 models.DateTimeField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slack_team',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='notify.slackteam')),
                ('slack_user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='notify.slackuser')),
            ],
        ),
    ]
