# Generated by Django 3.2.20 on 2024-04-07 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0074_auto_20240212_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='abstract',
            field=models.TextField(blank=True, help_text='Copying and pasting from word processors is supported.', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='abstract_cy',
            field=models.TextField(blank=True, help_text='Copying and pasting from word processors is supported.', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='abstract_de',
            field=models.TextField(blank=True, help_text='Copying and pasting from word processors is supported.', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='abstract_en',
            field=models.TextField(blank=True, help_text='Copying and pasting from word processors is supported.', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='abstract_en_us',
            field=models.TextField(blank=True, help_text='Copying and pasting from word processors is supported.', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='abstract_fr',
            field=models.TextField(blank=True, help_text='Copying and pasting from word processors is supported.', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='abstract_nl',
            field=models.TextField(blank=True, help_text='Copying and pasting from word processors is supported.', null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(help_text='Your article title', max_length=999),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_cy',
            field=models.CharField(help_text='Your article title', max_length=999, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_de',
            field=models.CharField(help_text='Your article title', max_length=999, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_en',
            field=models.CharField(help_text='Your article title', max_length=999, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_en_us',
            field=models.CharField(help_text='Your article title', max_length=999, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_fr',
            field=models.CharField(help_text='Your article title', max_length=999, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_nl',
            field=models.CharField(help_text='Your article title', max_length=999, null=True),
        ),
    ]
