class RomanNums:
    def __init__(self, roman_num):
        self.roman_num = roman_num
        self.droman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
                       'D': 500, 'M': 1000, 'IV': 4, 'IX': 9,
                       'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
                       }

    def from_roman(self):
        """Перевод римской записи числа в арабскую"""
        # todo Здесь нужно написать код
        result = 0
        c = 0
        number = self.roman_num
        while c < len(number):
            if c+1 < len(number) and number[c:c+2] in self.droman:
                result += self.droman[number[c:c+2]]
                c += 2
            else:
                result += self.droman[number[c]]
                c += 1
        return result

    def is_palindrome(self):
        """Является ли число палиндромом """
        # todo Здесь нужно написать код
        number = str(self.from_roman())
        return number == number[::-1]
