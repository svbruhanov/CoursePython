def get_list_info(lst):
    """Получение информации о списке
    :param lst: список из чисел
    :return: min_elem, max_elem, sum_list, average
    """
    # todo Здесь нужно написать код
    return (min(lst), max(lst), sum(lst), round(sum(lst)/len(lst), 2))
