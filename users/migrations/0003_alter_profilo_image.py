# Generated by Django 5.0.1 on 2024-02-06 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_profile_profilo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilo',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]
