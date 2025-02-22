# Generated by Django 3.0.7 on 2020-07-03 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0002_auto_20200703_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('code',
                 models.CharField(max_length=3,
                                  primary_key=True,
                                  serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='academy',
            name='state',
        ),
        migrations.AddField(
            model_name='academy',
            name='status',
            field=models.CharField(choices=[('INACTIVE', 'Inactive'),
                                            ('ACTIVE', 'Active'),
                                            ('DELETED', 'Deleted')],
                                   default='ACTIVE',
                                   max_length=15),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id',
                 models.AutoField(auto_created=True,
                                  primary_key=True,
                                  serialize=False,
                                  verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('country',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   to='admissions.Country')),
            ],
        ),
        migrations.AlterField(
            model_name='academy',
            name='city',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='admissions.City'),
        ),
        migrations.AlterField(
            model_name='academy',
            name='country',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to='admissions.Country'),
        ),
    ]
