def josephus_task(num_people, kill_num):
    """Задача Иосифа Флавия
    :param num_people: количество воинов
    :param kill_num: номер воина
    :return: номер последнего оставшегося воина
    """
    # todo Здесь нужно написать код
    res = 0
    for i in range(1, num_people + 1):
        res = (res + kill_num) % i
    return res + 1