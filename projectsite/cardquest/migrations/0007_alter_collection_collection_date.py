# Generated by Django 4.2.7 on 2023-12-26 17:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cardquest', '0006_collection_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='collection_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
