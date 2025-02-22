# Generated by Django 3.1.2 on 2020-11-05 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0011_auto_20201006_0058'),
        ('notify', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slackchannel',
            name='synqued_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='slackuser',
            name='synqued_at',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='slackchannel',
            name='cohort',
            field=models.OneToOneField(
                blank=True,
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to='admissions.cohort'),
            preserve_default=False,
        ),
    ]
