TEXT_DIGITS = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(search):
    """Возращает перевод числительного с англиского на русский c учетом болшой буквы
    :param search: искомое занечение
    :type search: str
    """
    try:
        if not search.islower():
            return TEXT_DIGITS[search.lower()].title()
        return TEXT_DIGITS[search.lower()]
    except BaseException:
        return None
