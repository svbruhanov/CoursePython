class PublicTransport:
    def __init__(self, brand, engine_power, year, color, max_speed):
        # todo Здесь нужно написать код
        self.brand = brand
        self._engine_power = engine_power
        self.year = year
        self.color = color
        self.max_speed = max_speed

    @property
    def info(self):
        """Информация о транспорте"""
        # todo Здесь нужно написать код
        return '{} {} {} {}'.format(self.brand, self.color, self.year, self._engine_power)


class Bus(PublicTransport):
    def __init__(self, brand, engine_power, year, color, max_speed, passengers, car_park, fare):
        super().__init__(brand, engine_power, year, color, max_speed)
        self.passengers = passengers
        self._Bus__park = car_park
        self._fare = fare
        # todo Здесь нужно написать код

    @property
    def park(self):
        """Парк приписки автобуса"""
        # todo Здесь нужно написать код
        return self._Bus__park

    @park.setter
    def park(self, park):
        self._Bus__park = park
        assert self._Bus__park > 1000
        assert self._Bus__park < 9999


class Tram(PublicTransport):
    def __init__(self, brand, engine_power, year, color, max_speed, route, path, fare):
        super().__init__(brand, engine_power, year, color, max_speed)
        self._Tram__route = route
        self.path = path
        self._fare = fare
        # todo Здесь нужно написать код

    @property
    def how_long(self):
        """Время прохождения маршрута"""
        # todo Здесь нужно написать код
        return self.max_speed/(4*self.path)
