# Generated by Django 5.0.4 on 2024-05-02 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_store_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='status',
        ),
    ]