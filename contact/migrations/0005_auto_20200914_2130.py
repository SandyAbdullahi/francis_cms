# Generated by Django 3.1.1 on 2020-09-14 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_serviceitem_serive_email_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serviceitem',
            old_name='serive_email_name',
            new_name='service_email_name',
        ),
    ]