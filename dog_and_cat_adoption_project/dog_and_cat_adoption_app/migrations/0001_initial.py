# Generated by Django 4.2.7 on 2023-11-04 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_type', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('breed', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=25)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
    ]
