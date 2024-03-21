def multiplication_chain(num):
    """Цепочка умножений
    :param num: положительное число
    :return: количество перемножений
    """
    # todo Здесь нужно написать код
    c = 0
    while len(str(num)) > 1:
        a = 1
        c += 1
        for i in str(num):
            a = a * int(i)
        num = a
    return c
