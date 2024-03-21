def everything_for_your_cat(cats_data):
    """Котики и их владельцы
    :param cats_data: информация о котах и их владельцах
    :return: информация о котах и их владельцах в виде строки
    """
    # todo Здесь нужно написать код
    d = {}
    for i in cats_data:
        name = i[-2] + ' ' + i[-1]
        if name in d:
            d[name] = d[name] + '; ' + i[0] + ', ' + str(i[1])
        else:
            d[name] = i[0] + ', ' + str(i[1])
    a = ''
    for i in d.keys():
        a += i + ': ' + d[i] + '\n'
    return a
('Алексей Егоров: Мартин, 5; Вася, 4\nАнна Самохина: Фродо, 3\n' 
 'Алексей Егоров: Мартин 5; Вася, 4\nАнна Самохина: Фродо 3\n')
