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


def num_translate(search):
    """Возращает перевод числительного с англиского на русский
    :param search: искомое занечение
    :type search: str
    """
    try:
        return TEXT_DIGITS[search]
    except BaseException:
        return None
