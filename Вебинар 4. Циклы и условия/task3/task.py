def sum_digits(num):
    """Нахождение суммы цифр числа
    :param num: число
    :return: сумма цифр числа
    """
    # todo Здесь нужно написать код

    num = str(num)
    num = sum([int(i) for i in num])
    return num

