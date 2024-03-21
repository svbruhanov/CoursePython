def which_triangle(a, b, c):
    """Определение типа треугольника
    :param a: длина стороны
    :param b: длина стороны
    :param c: длина стороны
    :return: тип треугольника
    """
    # todo Здесь нужно написать код
    if a+b>c and b+c>a and c+a>b:
        if a == b == c:
            return 'Равносторонний'
        if a == b or a == c or b == c:
            return  'Равнобедренный'
        return 'Обычный'
    return 'Не треугольник'

