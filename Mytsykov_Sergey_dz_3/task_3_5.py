from random import randint

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_part(item, joke, one_time):
    """Возращает часть щутки
        :param item: Возможные слова
        :param joke: Шутка
        :param one_time: Не повторять
        """
    key = randint(0, len(item) - 1)
    joke.append(item[key])
    if one_time:
        item.remove(item[key])


def get_jokes(count, one_time=False):
    """Возвращает набор шуток
    :param count: Количество шутк
    :param one_time: Не повторять
    """
    result = []
    for i in range(count):
        print(len(nouns))
        if len(nouns) == 0:
            break

        joke = []
        get_part(nouns, joke, one_time)
        get_part(adverbs, joke, one_time)
        get_part(adjectives, joke, one_time)

        result.append(' '.join(joke))

    return result
