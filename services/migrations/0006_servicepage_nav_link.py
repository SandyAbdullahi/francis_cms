# Generated by Django 3.1.1 on 2020-09-15 12:45

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_auto_20200913_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicepage',
            name='nav_link',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
