# Generated by Django 3.1.4 on 2021-01-28 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0013_auto_20210127_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='max_assistants_to_ask',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='survey',
            name='max_teachers_to_ask',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='answer',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'),
                                            ('SENT', 'Sent'),
                                            ('ANSWERED', 'Answered'),
                                            ('OPENED', 'Opened'),
                                            ('EXPIRED', 'Expired')],
                                   default='PENDING',
                                   max_length=15),
        ),
        migrations.AlterField(
            model_name='survey',
            name='avg_score',
            field=models.CharField(
                blank=True,
                default=None,
                editable=False,
                help_text=
                'The avg from all the answers taken under this survey',
                max_length=250,
                null=True),
        ),
    ]
