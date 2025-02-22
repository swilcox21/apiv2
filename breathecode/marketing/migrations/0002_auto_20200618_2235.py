# Generated by Django 3.0.7 on 2020-06-18 22:35

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='client_comments',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='course',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(default=None, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='latitude',
            field=models.DecimalField(decimal_places=6,
                                      default=None,
                                      max_digits=9,
                                      null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='longitude',
            field=models.DecimalField(decimal_places=6,
                                      default=None,
                                      max_digits=9,
                                      null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                default=None,
                max_length=128,
                null=True,
                region=None),
        ),
        migrations.AlterField(
            model_name='contact',
            name='state',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='street_address',
            field=models.CharField(default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='utm_campaign',
            field=models.CharField(default=None, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='utm_medium',
            field=models.CharField(default=None, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='utm_url',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='contact',
            name='zip_code',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
