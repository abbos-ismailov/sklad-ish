# Generated by Django 5.0.4 on 2024-05-02 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_store_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
