# Generated by Django 4.2.6 on 2023-10-24 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_area', models.PositiveIntegerField()),
                ('numer_of_bedrooms', models.BooleanField(default=False)),
                ('price', models.PositiveIntegerField()),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
    ]
