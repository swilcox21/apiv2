# Generated by Django 3.1.2 on 2020-10-12 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_auto_20201011_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='eventbrite_id',
            field=models.CharField(blank=True,
                                   default=None,
                                   max_length=80,
                                   null=True,
                                   unique=True),
        ),
        migrations.AddField(
            model_name='event',
            name='eventbrite_organizer_id',
            field=models.CharField(blank=True,
                                   default=None,
                                   max_length=80,
                                   null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='eventbrite_status',
            field=models.CharField(
                default='draft',
                help_text=
                'One of: draft, live, started, ended, completed and canceled',
                max_length=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='eventbrite_url',
            field=models.CharField(blank=True,
                                   default=None,
                                   max_length=255,
                                   null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='organizacion',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='events.organizacion'),
        ),
        migrations.AddField(
            model_name='event',
            name='published_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='sync_desc',
            field=models.TextField(blank=True,
                                   default=None,
                                   max_length=255,
                                   null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='sync_status',
            field=models.CharField(
                choices=[('PENDING', 'Pending'), ('PERSISTED', 'Persisted'),
                         ('ERROR', 'Error')],
                default='PENDING',
                help_text=
                'One of: PENDING, PERSISTED or ERROR depending on how the eventbrite sync status',
                max_length=9),
        ),
    ]
