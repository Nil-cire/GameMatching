# Generated by Django 2.2.5 on 2020-01-05 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PostAndSearch', '0016_auto_20200105_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='target',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='PostAndSearch.Target'),
        ),
    ]