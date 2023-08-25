# Generated by Django 4.2.4 on 2023-08-25 20:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DishModel',
            fields=[
                ('dishId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
