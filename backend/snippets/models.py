from django.core.validators import RegexValidator
from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class PhoneNumber(models.Model):
    """Модель номера телефона, указанного на странице."""

    number_regex = RegexValidator(
        regex=r'^(\+7|8|0)?(?:(\s|-)?\d{1,4}){2,4}$',
        message='Номер телефона может содержать только цифры, пробелы и дефисы',
    )
    number = models.CharField(
        'номер',
        validators=[number_regex],
        max_length=22,
    )

    panels = [
        FieldPanel('number'),
    ]

    class Meta:
        verbose_name = 'номер телефона'
        verbose_name_plural = 'номера телефонов'

    def __str__(self):
        return self.number
