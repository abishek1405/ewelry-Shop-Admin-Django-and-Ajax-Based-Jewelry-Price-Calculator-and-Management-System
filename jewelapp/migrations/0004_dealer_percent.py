# Generated by Django 4.1.6 on 2023-03-22 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelapp', '0003_dealer_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealer',
            name='percent',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]