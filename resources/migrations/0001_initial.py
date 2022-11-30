# Generated by Django 4.1.2 on 2022-11-30 18:58

import ckeditor.fields
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, choices=[('ur', 'Urgent'), ('ac', 'Acceptable'), ('op', 'Optimized')], max_length=200, null=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
                ('meta_title', models.CharField(blank=True, max_length=200)),
                ('type_of_resource', models.CharField(choices=[('E', 'Elements of a Paper'), ('R', 'Type of Research'), ('P', 'Type of Paper')], max_length=1)),
                ('meta_description', models.CharField(max_length=400)),
                ('content', ckeditor.fields.RichTextField(blank=True)),
                ('old_url', models.CharField(blank=True, max_length=200)),
                ('notes', models.TextField(blank=True, null=True)),
                ('resources_tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Resource',
                'verbose_name_plural': 'Resources',
            },
        ),
    ]
