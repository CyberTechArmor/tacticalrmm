# Generated by Django 3.2.6 on 2021-10-18 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0040_auto_20211010_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenthistory',
            name='username',
            field=models.CharField(default='system', max_length=255),
        ),
    ]