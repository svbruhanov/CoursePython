class Segment:
    def __init__(self, first_point, second_point):
        self.first_point = first_point
        self.second_point = second_point

    def length(self):
        """Вычисление длины отрезка"""
        # todo Здесь нужно написать код
        x1 = self.first_point[0]
        y1 = self.first_point[1]
        x2 = self.second_point[0]
        y2 = self.second_point[1]
        return round(((x1 - x2)**2 + (y1 - y2)**2)**0.5, 2)

    def x_axis_intersection(self):
        """Пересечение оси абсцисс"""
        # todo Здесь нужно написать код
        if (self.first_point[1] <= 0 <= self.second_point[1]) or (self.first_point[1] >= 0 >= self.second_point[1]):
            return True
        return False

    def y_axis_intersection(self):
        """Пересечение оси ординат"""
        # todo Здесь нужно написать код
        if (self.first_point[0] <= 0 <= self.second_point[0]) or (self.first_point[0] >= 0 >= self.second_point[0]):
            return True
        return False
