# Generated by Django 3.2.25 on 2024-03-18 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='../default_profile_zmipyy', upload_to='images/'),
        ),
    ]