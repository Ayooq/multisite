from wagtail.core.fields import RichTextField


class HeroFeaturesField(RichTextField):
    """Подкласс поля RichTextField для использования внутри HeroUnit.

    Ограничивает набор доступных средств форматирования текста.
    По умолчанию, набор состоит из следующих элементов:
        "bold" -- жирное начертание;
        "italic" -- курсивное начертание;
        "h2" -- заголовок второго уровня;
        "h3" -- заголовок третьего уровня;
        "h4" -- заголовок четвёртого уровня.
    Также устанавливает значение поля по умолчанию, пояснительный
    текст под окном редактора и наименование самого поля
    в административной панели:
        default='Lorem Ipsum',
        help_text='Подробная характеристика',
        verbose_name='особенности'
    """

    def __init__(self, *args, **kwargs):
        kwargs.update({
            'default': 'Lorem Ipsum',
            'features': [
                'bold',
                'italic',
                'h2',
                'h3',
                'h4',
            ],
            'help_text': 'Подробная характеристика',
            'verbose_name': 'особенности',
        })
        super().__init__(*args, **kwargs)
