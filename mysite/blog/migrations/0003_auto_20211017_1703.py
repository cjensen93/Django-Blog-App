# Generated by Django 3.2.7 on 2021-10-17 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_populate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='comment',
            name='posted',
            field=models.CharField(max_length=128),
        ),
    ]
