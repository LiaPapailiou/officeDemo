# Generated by Django 3.1.1 on 2020-09-27 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0014_remove_person_new_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='person_new_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='person_age',
            field=models.IntegerField(null=True),
        ),
    ]
