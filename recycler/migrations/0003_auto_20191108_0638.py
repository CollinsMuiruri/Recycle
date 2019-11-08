# Generated by Django 2.2.3 on 2019-11-08 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycler', '0002_auto_20191105_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='No description provided', max_length=500),
        ),
        migrations.AddField(
            model_name='product',
            name='mode_of_recycling',
            field=models.TextField(default='Send to our drop off points', max_length=50),
        ),
    ]