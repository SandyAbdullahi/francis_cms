# Generated by Django 3.1.1 on 2020-09-15 12:52

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_aboutpage_skills_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutpage',
            name='nav_link',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
