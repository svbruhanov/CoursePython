def memorize(function):
    # todo Здесь нужно написать код
    d = {}
    def wrapper(*args, **kwargs):
        res_func = function(*args, **kwargs)
        d.update({args: res_func})
        return res_func, d

    return wrapper
# todo Здесь ничего изменять не нужно!


@memorize
def get_kinetic_energy(weight, speed):
    """Кинетическая энергия
    :param weight: масса
    :param speed: скорость
    :return: кинетическую энергию
    """
    return (weight * speed ** 2)/2
