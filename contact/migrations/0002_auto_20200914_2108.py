# Generated by Django 3.1.1 on 2020-09-14 18:08

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactpage',
            name='body',
        ),
        migrations.AddField(
            model_name='contactpage',
            name='headline_message',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='headline_title',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
