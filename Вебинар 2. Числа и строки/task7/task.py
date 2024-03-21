def minimum_length_slice(first_string, second_string):
    """Срез минимальной длины
    :param first_string: первая строка
    :param second_string: вторая строка
    :return: min_slice срез минимальной длины строки second_string
    """
    # todo Здесь нужно написать код
    f = first_string
    s = second_string
    indexes = [s.index(i) for i in f]
    indexes.sort()
    min_slice = s[indexes[0]:indexes[-1]+1]
    return min_slice
