from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.images.blocks import ImageChooserBlock




class ServicePage(Page):
    #headline content
    headline_muted_text = RichTextField(blank=True)
    headline_title = RichTextField(blank=True)
    headline_intro = RichTextField(blank=True)
    headline_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    banner_text_title = RichTextField(blank=True)
    banner_text_content = RichTextField(blank=True)
    #service section content
    section_title = RichTextField(blank=True)
    service_one_title = RichTextField(blank=True)
    service_one_description = RichTextField(blank=True)
    service_one_image =  models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    service_two_title = RichTextField(blank=True)
    service_two_description = RichTextField(blank=True)
    service_two_image =  models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    service_three_title = RichTextField(blank=True)
    service_three_description = RichTextField(blank=True)
    service_three_image =  models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    call_to_action_title = RichTextField(blank=True)
    call_to_action_description = RichTextField(blank=True)

    








    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('headline_muted_text', classname="full"),
            FieldPanel('headline_title', classname="full"),
            FieldPanel('headline_intro', classname="full"),
            ImageChooserPanel('headline_image', classname="full"),
            FieldPanel('banner_text_title', classname="full"),
            FieldPanel('banner_text_content', classname="full"),
       ], heading="Headline Content"),
       MultiFieldPanel([
            FieldPanel('section_title', classname="full"),
            FieldPanel('service_one_title', classname="full"),
            FieldPanel('service_one_description', classname="full"),
            ImageChooserPanel('service_one_image', classname="full"),
            FieldPanel('service_two_title', classname="full"),
            FieldPanel('service_two_description', classname="full"),
            ImageChooserPanel('service_two_image', classname="full"),
            FieldPanel('service_three_title', classname="full"),
            FieldPanel('service_three_description', classname="full"),
            ImageChooserPanel('service_three_image', classname="full"),
       ], heading="Service Content"),
       MultiFieldPanel([
           FieldPanel('call_to_action_title', classname="full"),
           FieldPanel('call_to_action_description', classname="full"),
       ], heading="Call to Action Content")
    ]
