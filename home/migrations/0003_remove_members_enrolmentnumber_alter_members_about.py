# Generated by Django 4.0 on 2022-02-05 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_members_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='enrolmentNumber',
        ),
        migrations.AlterField(
            model_name='members',
            name='about',
            field=models.TextField(default=None),
        ),
    ]
