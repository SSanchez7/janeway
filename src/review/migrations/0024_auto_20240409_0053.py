# Generated by Django 3.2.20 on 2024-04-09 00:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review', '0023_auto_20240407_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='editorassignment',
            name='comments_for_editor',
            field=models.TextField(blank=True, help_text='If you have any comments for the Senior Editor you can add them here;                                            these will not be shared with the Author.', null=True, verbose_name='Comments for the Senior Editor'),
        ),
        migrations.AddField(
            model_name='editorassignment',
            name='date_accepted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='editorassignment',
            name='date_complete',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='editorassignment',
            name='date_declined',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='editorassignment',
            name='date_due',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='editorassignment',
            name='date_reminded',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='editorassignment',
            name='date_requested',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='editorassignment',
            name='decision',
            field=models.CharField(blank=True, choices=[('accept', 'Accept Without Revisions'), ('minor_revisions', 'Minor Revisions Required'), ('major_revisions', 'Major Revisions Required'), ('decline', 'Reject')], max_length=20, null=True, verbose_name='Recommendation'),
        ),
        migrations.AddField(
            model_name='editorassignment',
            name='for_author_consumption',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='editorassignment',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='editorassignment',
            name='senior_editor',
            field=models.ForeignKey(help_text='Senior Editor requesting the Assignment', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='senior_editor', to=settings.AUTH_USER_MODEL),
        ),
    ]
