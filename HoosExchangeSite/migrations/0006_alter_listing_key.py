# Generated by Django 4.1.7 on 2023-03-26 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HoosExchangeSite', '0005_listing_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='key',
            field=models.IntegerField(default=531895306),
        ),
    ]
