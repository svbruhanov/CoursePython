def flatten_and_sort(array):
    """Преобразование двумерного массива в плоский список
    :param array: двумерный массив
    :return: плоский список
    """
    # todo Здесь нужно написать код
    l = []
    for i in array:
        l.extend(i)
    l.sort()
    return l
