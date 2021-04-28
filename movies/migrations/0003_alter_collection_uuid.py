# Generated by Django 3.2 on 2021-04-26 18:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_collection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
