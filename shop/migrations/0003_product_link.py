# Generated by Django 2.0.2 on 2020-04-26 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200426_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='link',
            field=models.URLField(default='', max_length=250),
        ),
    ]
