# Generated by Django 4.2.7 on 2023-11-05 00:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dog_and_cat_adoption_app', '0005_pet_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='admin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pets', to=settings.AUTH_USER_MODEL),
        ),
    ]
