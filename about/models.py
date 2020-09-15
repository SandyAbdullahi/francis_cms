from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel



class AboutPage(Page):
    nav_link = RichTextField(blank=True)
    name = RichTextField(blank=True)
    my_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )   
    about_title = RichTextField(blank=True)
    about_bio = RichTextField(blank=True)
    skills_title = RichTextField(blank=True)
    skills_list = RichTextField(blank=True)
    call_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    call_me_title = RichTextField(blank=True)
    call_me_number = RichTextField(blank=True)










    content_panels = Page.content_panels + [
        MultiFieldPanel([
        FieldPanel('nav_link', classname="full"),
        FieldPanel('name', classname="full"),
        ImageChooserPanel('my_image', classname="full"),
        FieldPanel('about_title', classname="full"),
        FieldPanel('about_bio', classname="full"),
        ], heading="About content"),

        MultiFieldPanel([
        FieldPanel
        ('skills_title', classname="full"),
        FieldPanel('skills_list', classname="full"),
        ], heading="Skills section"),

        MultiFieldPanel([
        ImageChooserPanel('call_image', classname="full"),
        FieldPanel('call_me_title', classname="full"),
        FieldPanel('call_me_number', classname="full"),

        ], heading="Call content")

    ]