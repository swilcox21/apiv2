# Generated by Django 3.1.1 on 2020-09-14 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0002_auto_20200908_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='userspecialty',
            name='preview_url',
            field=models.CharField(blank=True,
                                   default=None,
                                   max_length=250,
                                   null=True),
        ),
    ]
