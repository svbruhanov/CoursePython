def move_zeros(lst):
    """Перемещение нулей
    :param lst: список из цифр
    :return: список из цифр с нулями в конце
    """
    # todo Здесь нужно написать код
    c = 0
    a = list(filter(lambda i: i!=0, lst))
    c = len(lst) - len(a)
    for i in range(c):
        a.append(0)
    return a
