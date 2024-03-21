class Trigon:
    def __init__(self, *args):
        # todo Здесь нужно написать код
        self.args = args
        if not all(isinstance(i, int) for i in self.args):
            raise TypeError('Стороны должны быть числами')
        if len([i for i in self.args if i <= 0]) > 0:
            raise ValueError('Стороны должны быть положительными')
        try:
            assert len(self.args) == 3
            a = self.args[0]
            b = self.args[1]
            c = self.args[2]
            if not (a + b > c and a + c > b and b + c > a):
                raise Exception('Не треугольник')
        except AssertionError:
            raise IndexError('Передано {} аргументов, а ожидается 3'.format(len(self.args)))
