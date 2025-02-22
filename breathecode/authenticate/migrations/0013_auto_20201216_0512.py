# Generated by Django 3.1.4 on 2020-12-16 05:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0012_auto_20201110_0727'),
    ]

    operations = [
        migrations.CreateModel(
            name='Capability',
            fields=[
                ('slug',
                 models.SlugField(max_length=25,
                                  primary_key=True,
                                  serialize=False)),
                ('description',
                 models.CharField(blank=True,
                                  default=None,
                                  max_length=255,
                                  null=True)),
            ],
        ),
        migrations.AddField(
            model_name='profileacademy',
            name='address',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profileacademy',
            name='first_name',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profileacademy',
            name='last_name',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profileacademy',
            name='phone',
            field=models.CharField(
                blank=True,
                default='',
                max_length=17,
                validators=[
                    django.core.validators.RegexValidator(
                        message=
                        "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
                        regex='^\\+?1?\\d{9,15}$')
                ]),
        ),
        migrations.AddField(
            model_name='role',
            name='capabilities',
            field=models.ManyToManyField(to='authenticate.Capability'),
        ),
    ]
