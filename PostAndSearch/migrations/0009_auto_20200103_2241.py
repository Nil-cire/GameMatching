# Generated by Django 2.2.5 on 2020-01-03 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostAndSearch', '0008_room_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='game_password',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
