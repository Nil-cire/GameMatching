# Generated by Django 2.2.5 on 2020-01-02 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostAndSearch', '0005_auto_20200102_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='create_time',
            field=models.DateTimeField(auto_created=True, null=True),
        ),
    ]
