# Generated by Django 2.2.5 on 2020-01-06 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PostAndSearch', '0017_auto_20200105_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='target',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PostAndSearch.Target'),
        ),
    ]