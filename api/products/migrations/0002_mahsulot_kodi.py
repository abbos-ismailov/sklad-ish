# Generated by Django 5.0.4 on 2024-05-01 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mahsulot',
            name='kodi',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]