# Generated by Django 5.0.1 on 2024-01-03 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eradah', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContainerLaunch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('launch_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ShippingRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cbm', models.DecimalField(decimal_places=2, max_digits=5, unique=True)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
