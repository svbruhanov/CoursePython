def segment(first_point, second_point):
    """Сумма всех координат точек
    :param first_point: координаты первой точки
    :param second_point: координаты второй точки
    :return: текст исключения наоборот или сумму всех координат
    """
    # todo Здесь нужно написать код
    try:
        x1, y1 = first_point
        x2, y2 = second_point
        s = x1 + y1 + x2 + y2
    except Exception as e:
        return e.__str__()[::-1]
    else:
        return s

