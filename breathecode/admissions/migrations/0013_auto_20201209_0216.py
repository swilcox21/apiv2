# Generated by Django 3.1.4 on 2020-12-09 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0012_auto_20201124_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academy',
            name='city',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='admissions.city'),
        ),
        migrations.AlterField(
            model_name='academy',
            name='country',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='admissions.country'),
        ),
    ]
