from collections import Counter

class PersonInfo:
    def __init__(self, fi, age, *deps):
        self.fi = fi
        self.age = age
        self.deps = deps

    def short_name(self):
        """Краткая запись Фамилия И."""
        # todo Здесь нужно написать код
        name = self.fi.split()
        return name[1] + ' ' + name[0][0] + '.'

    def path_deps(self):
        """Путь до подразделения"""
        # todo Здесь нужно написать код
        s = []
        for i in self.deps:
            s.append(i)
            s.append(' --> ')
        return "".join(s[:-1])

    def new_salary(self):
        """Новая зарплата"""
        # todo Здесь нужно написать код
        c = Counter(''.join(self.deps))
        a = sorted(list(c.values()))
        return sum(a[-3:]) * 1337 * self.age

