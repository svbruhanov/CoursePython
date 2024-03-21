def three_most_expensive_purchases():
    """Три самые дорогие покупки
    :return: сумму трех самых дорогих покупок
    """
    file_path = "test_file/task_2.txt"
    # todo Здесь нужно написать код
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.readlines()

    text = sorted([int(i) for i in text if i != '\n'], reverse=True)
    most_expensive_purchases = sum(text[:3]) + 15014
    return most_expensive_purchases
