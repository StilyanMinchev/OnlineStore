# Generated by Django 3.1.3 on 2020-12-01 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store_auth', '0002_auto_20201201_1328'),
        ('store', '0004_remove_watch_specifications'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watch',
            name='created_by',
        ),
        migrations.AddField(
            model_name='watch',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store_auth.userprofile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='watch',
            name='price',
            field=models.FloatField(),
        ),
    ]