# Generated by Django 4.2.16 on 2024-12-15 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0100_topicgroup_topics_accounttopic'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='study_topic',
            field=models.ManyToManyField(blank=True, null=True, through='core.AccountTopic', to='core.topics'),
        ),
    ]
