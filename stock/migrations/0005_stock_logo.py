# Generated by Django 3.2.7 on 2021-11-05 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_auto_20210928_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
