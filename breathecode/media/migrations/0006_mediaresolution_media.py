# Generated by Django 3.2 on 2021-06-03 22:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0005_auto_20210524_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediaresolution',
            name='media',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='media.media'),
        ),
    ]
