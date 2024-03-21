def to_roman(val):
    """Преобразование арабского числа в римское
    :param val: арабское число
    :return: римское число
    """
    # todo Здесь нужно написать код
    dt = {1: 'M', 2: 'MM', 3: 'MMM', 0: ''}
    ds = {1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM', 0: ''}
    dd = {1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC', 0: ''}
    de = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 0: ''}
    val = [int(i) for i in str(val)]
    a = []
    for i, v in enumerate(val[::-1]):
        if i == 0:
            a.append(de[v])
        elif i == 1:
            a.append(dd[v])
        elif i == 2:
            a.append(ds[v])
        elif i == 3:
            a.append(dt[v])
        else:
            ...
    return "".join(a[::-1])

