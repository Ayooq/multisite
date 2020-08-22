from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel,
)
from wagtail.core.models import Orderable, Page
from wagtail.images.edit_handlers import ImageChooserPanel

from page_components.models.components import HeroUnit, Section


class HomePage(HeroUnit, Page):
    """Модель домашней страницы."""

    max_count = 1
    parent_page_types = ['wagtailcore.Page']

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('summary'),
            FieldPanel('features'),
            ImageChooserPanel('background_image'),
        ], heading='целевая информация'),
        InlinePanel('sections', heading='разделы страницы', label='раздел'),
    ]

    settings_panels = []

    class Meta:
        verbose_name = 'Главная страница'


class HomePageSection(Section, Orderable):
    """Модель упорядоченного раздела домашней страницы."""

    page = ParentalKey(
        HomePage,
        on_delete=models.CASCADE,
        related_name='sections',
    )

    panels = [
        FieldPanel('heading'),
        FieldPanel('subheading'),
        StreamFieldPanel('body'),
    ]
