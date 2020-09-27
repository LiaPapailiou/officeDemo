# Generated by Django 3.1.1 on 2020-09-27 19:20

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0017_office_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office',
            name='peopleWorking',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=20), default=list, null=True, size=None),
        ),
    ]
