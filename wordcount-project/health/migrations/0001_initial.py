# Generated by Django 2.1.3 on 2019-11-17 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('name', models.CharField(max_length=40)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('ph', models.IntegerField()),
            ],
        ),
    ]
