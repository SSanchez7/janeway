# Generated by Django 4.2.16 on 2024-12-15 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('submission', '0084_remove_article_jats_article_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleAccountCI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='submission.article')),
            ],
            options={
                'unique_together': {('article', 'account')},
            },
        ),
        migrations.AddField(
            model_name='article',
            name='competing_interest_accounts',
            field=models.ManyToManyField(blank=True, null=True, related_name='competing_interest_accounts', through='submission.ArticleAccountCI', to=settings.AUTH_USER_MODEL),
        ),
    ]
