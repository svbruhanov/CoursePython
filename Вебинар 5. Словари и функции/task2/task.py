def repeats(our_str):
    """Повторы букв
    :param our_str: строка
    :return: новая строка с повторами букв
    """
    # todo Здесь нужно написать код
    d = { i : 0 for i in our_str}
    s = ''
    for i in our_str:
        d[i] += 1
        s += '{}_{}'.format(i, d[i])
    return s

