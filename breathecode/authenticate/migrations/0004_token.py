# Generated by Django 3.1 on 2020-08-14 04:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authenticate', '0003_auto_20200728_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('created',
                 models.DateTimeField(auto_now_add=True,
                                      verbose_name='Created')),
                ('key',
                 models.CharField(db_index=True, max_length=40, unique=True)),
                ('token_type',
                 models.CharField(default='temporal', max_length=64)),
                ('expires_at', models.CharField(max_length=64)),
                ('user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='auth_token',
                                   to=settings.AUTH_USER_MODEL,
                                   verbose_name='User')),
            ],
            options={
                'unique_together': {('user', 'token_type')},
            },
        ),
    ]
