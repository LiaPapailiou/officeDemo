# Generated by Django 3.1.1 on 2020-09-24 18:10

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0007_office_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='office',
            name='employee',
        ),
        migrations.AddField(
            model_name='person',
            name='office',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='office.office'),
        ),
        migrations.AlterField(
            model_name='office',
            name='peopleWorking',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, default='list', size=None),
        ),
    ]