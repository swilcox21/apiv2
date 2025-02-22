# Generated by Django 3.0.8 on 2020-07-17 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authenticate', '0002_credentialsquickbooks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('status',
                 models.CharField(choices=[('DUE', 'Due'), ('PAID', 'Paid')],
                                  default='DUE',
                                  max_length=20)),
                ('total_duration_in_minutes', models.FloatField()),
                ('total_price', models.FloatField()),
                ('paid_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('price_per_hour', models.FloatField()),
                ('github_user',
                 models.ForeignKey(
                     default=None,
                     null=True,
                     on_delete=django.db.models.deletion.SET_DEFAULT,
                     to='authenticate.CredentialsGithub')),
                ('user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('status',
                 models.CharField(choices=[
                     ('DRAFT', 'Draft'), ('TODO', 'Todo'), ('DOING', 'Doing'),
                     ('DONE', 'Done')
                 ],
                                  default='DRAFT',
                                  max_length=20)),
                ('github_state', models.CharField(max_length=30)),
                ('github_number', models.PositiveIntegerField()),
                ('body', models.TextField()),
                ('duration_in_minutes', models.FloatField()),
                ('url', models.URLField(max_length=255)),
                ('repository_url', models.URLField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to=settings.AUTH_USER_MODEL)),
                ('bill',
                 models.ForeignKey(default=None,
                                   null=True,
                                   on_delete=django.db.models.deletion.CASCADE,
                                   to='freelance.Bill')),
                ('freelancer',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='freelance.Freelancer')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='freelancer',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='freelance.Freelancer'),
        ),
        migrations.AddField(
            model_name='bill',
            name='reviewer',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL),
        ),
    ]
