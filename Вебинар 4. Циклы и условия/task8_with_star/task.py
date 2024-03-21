def max_division_by_3(num):
    """Преобразование числа
    :param num: натуральное число
    :return: другое натуральное число, удовлетворяющее условиям
    """
    # todo Здесь нужно написать код
    s = str(num)
    for i in range(len(s)):
        for j in range(9, int(s[i]), -1):
            c = s[:i] + str(j) + s[i+1:]
            if int(c) % 3 == 0:
                return int(c)
