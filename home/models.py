from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    headline = RichTextField(blank=True)
    headline_intro = RichTextField(blank=True)
    headline_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    muted_text_top = RichTextField(blank=True)
    top_sentence = RichTextField(blank=True)

    
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('headline', classname="full"),
        FieldPanel('headline_intro', classname="full"),
        FieldPanel('headline_image', classname="full"),
        FieldPanel('muted_text_top', classname="full"),
        FieldPanel('top_sentence', classname="full"),
        FieldPanel('body', classname="full"),
    ]