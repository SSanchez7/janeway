# Generated by Django 3.2.20 on 2024-05-06 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0041_auto_20231207_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preprint',
            name='abstract',
            field=models.TextField(blank=True, help_text='Copying and pasting from word processors is supported.', null=True),
        ),
    ]