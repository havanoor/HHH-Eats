# Generated by Django 3.1.2 on 2020-11-05 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0005_restaurant_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('val', models.ManyToManyField(to='foodapp.Item')),
            ],
        ),
    ]
