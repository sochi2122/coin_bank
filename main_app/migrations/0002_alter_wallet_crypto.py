# Generated by Django 4.0.2 on 2022-03-12 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='crypto',
            field=models.ManyToManyField(through='main_app.Amount', to='main_app.Crypto'),
        ),
    ]
