from django.db import models
from wagtail.core.fields import StreamField
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock

from .blocks import ParagraphBlock
from .fields import HeroFeaturesField


class HeroUnit(models.Model):
    """Модель титульного баннера посадочной страницы."""

    summary = models.CharField(
        'заглавный текст',
        help_text='Суть продукта/услуги',
        max_length=100,
        default='Lorem Ipsum',
    )
    features = HeroFeaturesField(
        blank=True,
    )
    background_image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+',
        verbose_name='фоновое изображение',
    )

    class Meta:
        abstract = True


class Section(models.Model):
    """Модель тематического раздела страницы."""

    heading = models.CharField(
        'заголовок',
        help_text='Тема раздела',
        max_length=100,
        default='Lorem Ipsum',
    )
    subheading = models.CharField(
        'подзаголовок',
        max_length=80,
        default='Lorem Ipsum',
        blank=True,
    )
    body = StreamField(
        [
            ('paragraph', ParagraphBlock()),
            ('image', ImageChooserBlock(
                label='Изображение',
                help_text='Иллюстрирование текста',
            )),
            ('embed', EmbedBlock(
                label='Встраиваемое медиа',
                help_text='Например, видео с YouTube',
            )),
        ],
        verbose_name='содержание',
    )

    class Meta:
        abstract = True
