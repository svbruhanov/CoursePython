def test_file_path(file_path):
    """Путь до файла
    :param file_path: абсолютный путь до файла
    :return: название файла без расширения, названия диска и корневую папку
    """
    # todo Здесь нужно написать код
    s = file_path.split('\\')
    a = s[-1]
    #a = a.replace('_', '.')
    a = a.split('.txt')
    a = a[0].split('.py')
    a = a[0].split('.exe')
    file_name = a[0]
    disk_name = s[0][0]
    root_folder = s[1]
    return file_name, disk_name, root_folder
