# Generated by Django 2.2.5 on 2020-01-03 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PostAndSearch', '0010_auto_20200103_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='target',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PostAndSearch.Target'),
        ),
    ]
