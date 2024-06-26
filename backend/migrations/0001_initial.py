# Generated by Django 5.0.6 on 2024-05-20 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock_name', models.CharField(max_length=25)),
                ('date', models.DateField()),
                ('open_price', models.FloatField()),
                ('highest_price', models.FloatField()),
                ('lowest_price', models.FloatField()),
                ('close_price', models.FloatField()),
                ('volume', models.FloatField()),
                ('dividends', models.FloatField()),
                ('stock_splits', models.FloatField()),
            ],
        ),
    ]
