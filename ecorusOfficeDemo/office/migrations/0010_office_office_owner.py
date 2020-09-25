# Generated by Django 3.1.1 on 2020-09-25 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('office', '0009_remove_office_office_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='office_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='office', to=settings.AUTH_USER_MODEL),
        ),
    ]