# Generated by Django 3.1.1 on 2020-09-12 17:42

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20200912_2007'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicepage',
            name='banner_text_content',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='servicepage',
            name='banner_text_title',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
