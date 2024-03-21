def even_sum(lst):
    """Получение суммы элементов списка с четными индексами
    :param lst: список из чисел
    :return: сумму элементов с четными индексами
    """
    # todo Здесь нужно написать код

    return sum([ i for i in lst if lst.index(i) % 2 == 0])
