def letter_stat(our_str):
    """Буквенная статистика
    :param our_str: строка
    :return: словарь со статистикой по буквам
    """
    # todo Здесь нужно написать код
    return { i : our_str.count(i) for i in our_str}

