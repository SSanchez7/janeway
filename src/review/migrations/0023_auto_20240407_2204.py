# Generated by Django 3.2.20 on 2024-04-07 22:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0075_auto_20240407_2204'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('review', '0022_remove_reviewform_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decisiondraft',
            name='decision',
            field=models.CharField(choices=[('accept', 'Accept Without Revisions'), ('minor_revisions', 'Minor Revisions Required'), ('major_revisions', 'Major Revisions Required'), ('decline', 'Reject')], max_length=100, verbose_name='Draft Decision'),
        ),
        migrations.AlterField(
            model_name='decisiondraft',
            name='editor_decision',
            field=models.CharField(blank=True, choices=[('accept', 'Accept'), ('decline', 'Decline')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='editorassignment',
            name='editor_type',
            field=models.CharField(choices=[('editor', 'Editor'), ('section-editor', 'Section Editor'), ('senior-editor', 'Senior Editor')], max_length=20),
        ),
        migrations.AlterField(
            model_name='revisionrequest',
            name='editor_note',
            field=models.TextField(blank=True, help_text='You can use this optional field to provide the author with any information that may help them when evaluating the article reviews and integrating changes into their manuscript. This text will be displayed to the author on  the revision page, above the reviews.', null=True),
        ),
        migrations.AlterField(
            model_name='revisionrequest',
            name='type',
            field=models.CharField(choices=[('minor_revisions', 'Minor Revisions'), ('major_revisions', 'Major Revisions')], default='minor_revisions', max_length=20),
        ),
        migrations.CreateModel(
            name='SeniorEditorAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned', models.DateTimeField(default=django.utils.timezone.now)),
                ('notified', models.BooleanField(default=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='submission.article')),
                ('senior_editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('article', 'senior_editor')},
            },
        ),
    ]
