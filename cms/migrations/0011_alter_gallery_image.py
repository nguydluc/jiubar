# Generated by Django 5.0.2 on 2024-02-15 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0010_alter_gallery_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to='static/img/'),
        ),
    ]
