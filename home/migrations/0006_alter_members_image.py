# Generated by Django 4.0 on 2022-02-18 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_members_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]