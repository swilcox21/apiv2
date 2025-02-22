# Generated by Django 3.1.4 on 2020-12-28 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0008_userspecialty_status_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='userspecialty',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'),
                                            ('PERSISTED', 'Persisted'),
                                            ('ERROR', 'Error')],
                                   default='PENDING',
                                   max_length=15),
        ),
    ]
