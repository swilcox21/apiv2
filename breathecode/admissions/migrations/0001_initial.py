# Generated by Django 3.0.7 on 2020-06-16 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Academy',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('slug', models.CharField(max_length=150, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('street_address', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('latitude', models.DecimalField(decimal_places=6,
                                                 max_digits=9)),
                ('longitude',
                 models.DecimalField(decimal_places=6, max_digits=9)),
                ('state', models.CharField(max_length=30)),
                ('zip_code', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('logistical_information', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('slug', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=150)),
                ('logo', models.CharField(blank=True, max_length=250)),
                ('duration_in_hours', models.IntegerField()),
                ('duration_in_days', models.IntegerField()),
                ('week_hours', models.IntegerField()),
                ('description', models.TextField(max_length=450)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('slug', models.CharField(max_length=150, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('kickoff_date', models.DateTimeField()),
                ('ending_date', models.DateTimeField()),
                ('current_day', models.IntegerField()),
                ('stage',
                 models.CharField(choices=[('INACTIVE', 'Inactive'),
                                           ('PREWORK', 'Prework'),
                                           ('STARTED', 'Started'),
                                           ('FINAL_PROJECT', 'Final Project'),
                                           ('ENDED', 'Ended'),
                                           ('DELETED', 'Deleted')],
                                  default='INACTIVE',
                                  max_length=15)),
                ('language', models.CharField(default='en', max_length=2)),
                ('online_room_url',
                 models.CharField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('academy',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='admissions.Academy')),
                ('certificate',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='admissions.Certificate')),
            ],
        ),
        migrations.CreateModel(
            name='CohortUser',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('role',
                 models.CharField(choices=[('TEACHER', 'Teacher'),
                                           ('ASSISTANT', 'Assistant'),
                                           ('STUDENT', 'Student')],
                                  default='STUDENT',
                                  max_length=9)),
                ('finantial_status',
                 models.CharField(choices=[('FULLY_PAID', 'Fully Paid'),
                                           ('UP_TO_DATE', 'Up to date'),
                                           ('LATE', 'Late')],
                                  default=None,
                                  max_length=15,
                                  null=True)),
                ('educational_status',
                 models.CharField(choices=[('ACTIVE', 'Active'),
                                           ('POSTPONED', 'Postponed'),
                                           ('GRADUATED', 'Graduated'),
                                           ('DROPPED', 'Dropped')],
                                  default=None,
                                  max_length=15,
                                  null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cohort',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='admissions.Cohort')),
                ('user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AcademyCertificate',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('academy',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='admissions.Academy')),
                ('certificate',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='admissions.Certificate')),
            ],
        ),
    ]
