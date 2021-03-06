# Generated by Django 4.0.2 on 2022-04-02 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctorname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='fees',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='specialization',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
