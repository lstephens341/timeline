# Generated by Django 2.1.3 on 2020-04-17 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photoupload', '0008_auto_20200209_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.CharField(default='', max_length=200),
        ),
    ]