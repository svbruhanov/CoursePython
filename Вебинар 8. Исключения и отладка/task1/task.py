def treatment_sum(our_tuple):
    """Обработка суммы элементов кортежа
    :param our_tuple: кортеж
    :return: сумму элементов кортежа
    """
    # todo Здесь нужно написать код
    try:
        if len(our_tuple) > 2:
            raise Exception('Много данных')
        a = our_tuple[0]
        b = our_tuple[1]
        res = a + b
    except TypeError:
        return 'Нельзя сложить эти данные'
    except IndexError:
        return 'Недостаточно данных'
    else:
        return res
