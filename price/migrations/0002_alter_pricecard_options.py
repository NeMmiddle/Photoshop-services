# Generated by Django 4.0.5 on 2022-07-03 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pricecard',
            options={'verbose_name': 'Цены', 'verbose_name_plural': 'Цены'},
        ),
    ]
