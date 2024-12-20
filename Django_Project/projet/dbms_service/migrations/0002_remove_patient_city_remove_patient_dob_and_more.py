# Generated by Django 5.1.3 on 2024-11-15 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbms_service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='city',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='email',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='region',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='street',
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='region',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='street',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
