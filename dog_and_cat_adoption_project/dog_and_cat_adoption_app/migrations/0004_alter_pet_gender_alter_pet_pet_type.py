# Generated by Django 4.2.7 on 2023-11-04 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog_and_cat_adoption_app', '0003_remove_pet_status_pet_adoption_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=10),
        ),
        migrations.AlterField(
            model_name='pet',
            name='pet_type',
            field=models.CharField(choices=[('dog', 'Dog'), ('cat', 'Cat')], default='dog', max_length=10),
        ),
    ]
