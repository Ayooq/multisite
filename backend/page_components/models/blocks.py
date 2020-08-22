from wagtail.core.blocks import RichTextBlock


class ParagraphBlock(RichTextBlock):
    """Подкласс RichTextBlock поля StreamField для форматирования параграфа.

    Ограничивает набор доступных средств форматирования текста.
    По умолчанию, набор состоит из следующих элементов:
        "bold" -- жирное начертание;
        "italic" -- курсивное начертание;
        "h2" -- заголовок второго уровня;
        "h3" -- заголовок третьего уровня;
        "h4" -- заголовок четвёртого уровня.
    Также устанавливает значение поля по умолчанию, пояснительный
    текст под окном редактора и наименование самого блока
    в административной панели:
        default='Lorem Ipsum',
        help_text='Текстовый абзац',
        label='Параграф'
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
            'help_text': 'Текстовый абзац',
            'label': 'Параграф',
        })
        super().__init__(*args, **kwargs)
