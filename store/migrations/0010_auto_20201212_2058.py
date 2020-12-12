# Generated by Django 3.1.3 on 2020-12-12 18:58

from django.db import migrations, models
import store.validators


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20201212_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watch',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='watch',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, validators=[store.validators.positive_number]),
        ),
    ]