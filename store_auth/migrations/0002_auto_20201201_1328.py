# Generated by Django 3.1.3 on 2020-12-01 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='profiles/'),
        ),
    ]