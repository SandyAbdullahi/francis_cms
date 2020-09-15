from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel



class HomePageCarouselImages(Orderable):
    """
        Between 1 and 20 images for the home page carousel
    """
    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        ImageChooserPanel("carousel_image", classname="full")
    ]


class HomePage(Page):
    nav_link= RichTextField(blank=True)
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
    work_feature_one_title = RichTextField(blank=True)
    work_feature_one_description = RichTextField(blank=True)
    work_feature_one_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    work_feature_two_title = RichTextField(blank=True)
    work_feature_two_description = RichTextField(blank=True)
    work_feature_two_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    work_feature_three_title = RichTextField(blank=True)
    work_feature_three_description = RichTextField(blank=True)
    work_feature_three_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    work_feature_four_title = RichTextField(blank=True)
    work_feature_four_description = RichTextField(blank=True)
    work_feature_four_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    
    

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('nav_link', classname="full"),
            FieldPanel('headline', classname="full"),
            FieldPanel('headline_intro', classname="full"),
            ImageChooserPanel('headline_image', classname="full"),
        ], heading="Headline Content"),
        MultiFieldPanel([
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
        ], heading="Intro Content"),
        MultiFieldPanel([
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
        ], heading="Service Content"),
        MultiFieldPanel([
            FieldPanel('work_title', classname="full"),
            FieldPanel('work_content', classname="full"),
            FieldPanel('work_feature_one_title', classname="full"),
            FieldPanel('work_feature_one_description', classname="full"),
            ImageChooserPanel('work_feature_one_image', classname="full"),
            FieldPanel('work_feature_two_title', classname="full"),
            FieldPanel('work_feature_two_description', classname="full"),
            ImageChooserPanel('work_feature_two_image', classname="full"),
            FieldPanel('work_feature_three_title', classname="full"),
            FieldPanel('work_feature_three_description', classname="full"),
            ImageChooserPanel('work_feature_three_image', classname="full"),
            FieldPanel('work_feature_four_title', classname="full"),
            FieldPanel('work_feature_four_description', classname="full"),
            ImageChooserPanel('work_feature_four_image', classname="full"),


        ], heading="Work Features"),
        MultiFieldPanel([
        InlinePanel('carousel_images', max_num=20, min_num=1, label="add image"),
        ], heading="Carousel Images")



   
    ]