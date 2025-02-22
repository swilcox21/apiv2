# Generated by Django 3.1.4 on 2021-01-27 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0007_auto_20201222_0949'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonitorScript',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('script_slug',
                 models.SlugField(blank=True, default=None, null=True)),
                ('script_body',
                 models.TextField(blank=True, default=None, null=True)),
                ('frequency_delta',
                 models.DurationField(
                     default='00:30:00',
                     help_text=
                     'How long to wait for the next execution, defaults to 30 minutes'
                 )),
                ('status_code', models.FloatField(default=200)),
                ('severity_level', models.IntegerField(default=0)),
                ('status_text',
                 models.CharField(blank=True,
                                  default=None,
                                  editable=False,
                                  max_length=255,
                                  null=True)),
                ('special_status_text',
                 models.CharField(
                     blank=True,
                     default=None,
                     help_text='Add a message for people to see when is down',
                     max_length=255,
                     null=True)),
                ('response_text',
                 models.TextField(blank=True, default=None, null=True)),
                ('last_run',
                 models.DateTimeField(blank=True, default=None, null=True)),
                ('status',
                 models.CharField(choices=[('OPERATIONAL', 'Operational'),
                                           ('MINOR', 'Minor'),
                                           ('CRITICAL', 'Critical')],
                                  default='OPERATIONAL',
                                  max_length=20)),
                ('paused_until',
                 models.DateTimeField(
                     blank=True,
                     default=None,
                     help_text=
                     'if you want to stop checking for a period of time',
                     null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('application',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='monitoring.application')),
            ],
        ),
    ]
