# Generated by Django 2.2.5 on 2020-01-04 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostAndSearch', '0011_auto_20200103_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
