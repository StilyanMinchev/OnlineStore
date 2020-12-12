# Generated by Django 3.1.3 on 2020-12-10 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store_auth', '0002_auto_20201201_1328'),
        ('store', '0007_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.watch')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store_auth.userprofile')),
            ],
        ),
    ]
