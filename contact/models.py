from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class ContactPage(Page):
   
    headline_title = RichTextField(blank=True)
    headline_message = RichTextField(blank=True)





    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('headline_title', classname="full"),
            FieldPanel('headline_message', classname="full"),
        ], heading="Headline Content")
    ]

class ServiceItem(Page):
    service_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    service_email_name = RichTextField(blank=True)
    service_title = RichTextField(blank=True)
    service_description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
       MultiFieldPanel([
        ImageChooserPanel("service_image", classname="full"),
        FieldPanel('service_email_name', classname="full"),
        FieldPanel('service_title', classname="full"),
        FieldPanel('service_description', classname="full"),
       ], heading="Service choices")

    ]