def quadratic(b, c):
    """Решение квадратного уравнения
    :param b: коэффициент b
    :param c: коэффициент c
    :return: корни квадратного уравнения
    """
    # todo Здесь нужно написать код
    discriminant = b*b - 4 * c
    droot = (discriminant ** 0.5)
    d1 = (-b - droot)
    d2 = (-b + droot)
    a1 = d1 / 2
    x1 = round(a1, 2)
    a2 = d2 / 2
    x2 = round(a2, 2)
    return x2, x1
