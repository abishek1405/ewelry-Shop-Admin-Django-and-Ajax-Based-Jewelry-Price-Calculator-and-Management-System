# Generated by Django 4.1.6 on 2023-03-22 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jewelapp', '0002_dealer'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealer',
            name='created_at',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
