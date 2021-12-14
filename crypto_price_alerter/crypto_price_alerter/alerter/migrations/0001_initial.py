# Generated by Django 3.1.4 on 2021-12-14 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=20)),
                ('alert_price', models.FloatField()),
                ('email_sent', models.BooleanField()),
                ('timestamp', models.DateField(auto_now=True)),
            ],
        ),
    ]
