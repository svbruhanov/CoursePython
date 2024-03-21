def modification(lst):
    """Изменение списка
    :param lst: список
    :return: преобразованный список
    """
    # todo Здесь нужно написать код
    a = lst[1:-1]
    a.insert(0, lst[-1])
    a.append(lst[0])
    return a
