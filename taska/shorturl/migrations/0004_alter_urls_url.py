# Generated by Django 4.0.1 on 2022-07-11 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shorturl', '0003_urls_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='url',
            field=models.CharField(max_length=300, verbose_name='URL'),
        ),
    ]