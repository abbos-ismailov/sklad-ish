# Generated by Django 5.0.4 on 2024-05-01 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_xomashyomahsulot_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='status',
        ),
    ]
