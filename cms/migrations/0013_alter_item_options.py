# Generated by Django 5.0.2 on 2024-02-19 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_alter_gallery_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'Menu Item', 'verbose_name_plural': 'Menu Items'},
        ),
    ]
