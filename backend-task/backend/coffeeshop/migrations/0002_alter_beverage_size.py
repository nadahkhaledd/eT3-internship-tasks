# Generated by Django 4.0.3 on 2022-07-30 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beverage',
            name='size',
            field=models.CharField(max_length=300),
        ),
    ]
