# Generated by Django 3.2.25 on 2024-03-18 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='../default-profile_rgasqm', upload_to='images/'),
        ),
    ]
