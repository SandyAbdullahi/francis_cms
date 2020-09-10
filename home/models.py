from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel



class HomePage(Page):
    headline = RichTextField(blank=True)
    headline_intro = RichTextField(blank=True)
    headline_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    muted_text_top = RichTextField(blank=True)
    top_sentence = RichTextField(blank=True)
    top_sentence_second = RichTextField(blank=True)
    number_one = RichTextField(blank=True)
    number_one_title = RichTextField(blank=True)
    number_one_content = RichTextField(blank=True)
    number_two = RichTextField(blank=True)
    number_two_title = RichTextField(blank=True)
    number_two_content = RichTextField(blank=True)
    number_three = RichTextField(blank=True)
    number_three_title = RichTextField(blank=True)
    number_three_content = RichTextField(blank=True)
    muted_text_bottom = RichTextField(blank=True)
    service_title = RichTextField(blank=True)
    service_content = RichTextField(blank=True)
    service_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    point_one_title = RichTextField(blank=True)
    point_one_content = RichTextField(blank=True)
    point_two_title = RichTextField(blank=True)
    point_two_content = RichTextField(blank=True)
    point_three_title = RichTextField(blank=True)
    point_three_content = RichTextField(blank=True)
    work_title = RichTextField(blank=True)
    work_content = RichTextField(blank=True)
    
    

    content_panels = Page.content_panels + [
        FieldPanel('headline', classname="full"),
        FieldPanel('headline_intro', classname="full"),
        ImageChooserPanel('headline_image', classname="full"),
        FieldPanel('muted_text_top', classname="full"),
        FieldPanel('top_sentence', classname="full"),
        FieldPanel('top_sentence_second', classname="full"),
        FieldPanel('number_one', classname="full"),
        FieldPanel('number_one_title', classname="full"),
        FieldPanel('number_one_content', classname="full"),
        FieldPanel('number_two', classname="full"),
        FieldPanel('number_two_title', classname="full"),
        FieldPanel('number_two_content', classname="full"),
        FieldPanel('number_three', classname="full"),
        FieldPanel('number_three_title', classname="full"),
        FieldPanel('number_three_content', classname="full"),
        FieldPanel('muted_text_bottom', classname="full"),
        FieldPanel('service_title', classname="full"),
        FieldPanel('service_content', classname="full"),
        ImageChooserPanel('service_image', classname="full"),
        FieldPanel('point_one_title', classname="full"),
        FieldPanel('point_one_content', classname="full"),
        FieldPanel('point_two_title', classname="full"),
        FieldPanel('point_two_content', classname="full"),
        FieldPanel('point_three_title', classname="full"),
        FieldPanel('point_three_content', classname="full"),
        FieldPanel('work_title', classname="full"),
        FieldPanel('work_content', classname="full"),



   
    ]