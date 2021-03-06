# Generated by Django 3.1.1 on 2020-09-09 18:38

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0022_uploadedimage'),
        ('wagtailcore', '0052_pagelogentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('headline', wagtail.core.fields.RichTextField(blank=True)),
                ('headline_intro', wagtail.core.fields.RichTextField(blank=True)),
                ('muted_text_top', wagtail.core.fields.RichTextField(blank=True)),
                ('top_sentence', wagtail.core.fields.RichTextField(blank=True)),
                ('body', wagtail.core.fields.RichTextField(blank=True)),
                ('headline_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
