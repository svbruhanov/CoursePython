def create_phone_number(num_tuple):
    """Создание номера телефона
    :param num_tuple: кортеж из цифр
    :return: строку в виде номера телефона
    """
    # todo Здесь нужно написать код
    s = ''.join([str(i) for i in num_tuple])
    t = s[:3]
    y = s[3: 6]
    u = s[6:]
    a = '({}) {}-{}'.format(t, y, u)
    return a
