import math
from abc import ABC


# принимает аргументы
class Arguments:
    def __init__(self, first, second=0):
        self.first = first
        self.second = second


class Operation(ABC):
    def calculate(self):
        pass


class Minus(Operation):
    def __init__(self, arguments: Arguments):
        self.arguments = arguments

    def calculate(self):
        return self.arguments.first - self.arguments.second


class Plus(Operation):
    def __init__(self, arguments: Arguments):
        self.arguments = arguments

    def calculate(self):
        return self.arguments.first + self.arguments.second


class Multi(Operation):
    def __init__(self, arguments: Arguments):
        self.arguments = arguments

    def calculate(self):
        return self.arguments.first * self.arguments.second


class Division(Operation):
    def __init__(self, arguments: Arguments):
        self.arguments = arguments


    def calculate(self):
        if self.arguments.second: return round(self.arguments.first / self.arguments.second, 6)
        return 'Делить на ноль нельзя!'


class Remains(Operation):
    def __init__(self, arguments: Arguments):
        self.arguments = arguments

    def calculate(self):
        if self.arguments.second: return self.arguments.first % self.arguments.second
        return 'Делить на ноль нельзя!'


class Ln(Operation):
    def __init__(self, arguments: Arguments):
        self.arguments = arguments

    def calculate(self):
        if self.arguments.first > 0: return round(math.log(self.arguments.first), 6)
        return 'Невозможно вычислить log'


class Lg(Operation):
    def __init__(self, arguments: Arguments):
        self.arguments = arguments

    def calculate(self):
        if self.arguments.first > 0: return round(math.log(self.arguments.first, 10), 6)
        return 'Невозможно вычислить log'


class Log(Operation):
    def __init__(self, arguments: Arguments):
        self.arguments = arguments

    def calculate(self):
        if 'e' in str(self.arguments.first).lower() or 'е' in str(self.arguments.first).lower():
            self.arguments.first = math.e ** int(str(self.arguments.first).split('^')[1])
            return self.calculate()
        elif (self.arguments.second == 'e' or self.arguments.second == 'е') and self.arguments.first > 0:
            return round(math.log(self.arguments.first), 6)
        elif self.arguments.first > 0 and self.arguments.second > 0 and self.arguments.second != 1:
            return round(math.log(self.arguments.first, self.arguments.second), 6)
        return 'Невозможно вычислить log'


class Exponentiation(Operation):
    def __init__(self, arguments: Arguments):
        self.arguments = arguments

    def calculate(self):
        if 'e' in str(self.arguments.first).lower() or 'е' in str(self.arguments.first).lower():
            return self.calculate(math.e ** int(str(self.arguments.first).split('^')[1]))
        return round(self.arguments.first ** self.arguments.second, 6)


class Sqrt(Operation):
    def __init__(self, arguments: Arguments):
        self.arguments = arguments

    def calculate(self):
        if self.arguments.first > 0: return round(self.arguments.first ** 0.5, 6)
        return 'невозможно извлечь корень!'


class Cos(Operation):
    def __init__(self, arguments: Arguments):
        self.arguments = arguments

    def calculate(self):
        return round(math.cos(self.arguments.first), 6)


class Sin(Operation):
    def __init__(self, arguments: Arguments):
        self.arguments = arguments

    def calculate(self):
        return round(math.sin(self.arguments.first), 6)


class Combination(Operation):
    def __init__(self, arguments: Arguments):
        self.arguments = arguments

    def calculate(self):
        return math.comb(self.arguments.first, self.arguments.second)


class Factorial(Operation):
    def __init__(self, arguments: Arguments):
        self.arguments = arguments

    def calculate(self):
        return math.factorial(self.arguments.first)


class Acos(Operation):
    def __init__(self, arguments: Arguments):
        self.arguments = arguments

    def calculate(self):
        if 0 <= self.arguments.first <= 1: return round(math.acos(self.arguments.first), 6)
        return 'cos не определен'


class Asin(Operation):
    def __init__(self, arguments: Arguments):
        self.arguments = arguments

    def calculate(self):
        if 0 <= self.arguments.first <= 1: return round(math.asin(self.arguments.first), 6)
        return 'sin не определен'


print(Asin(Arguments(5)).calculate())
