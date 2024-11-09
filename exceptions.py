"""importing maths"""
import math
def division(a, b):
    """Checking for exceptions in division"""
    if b == 0:
        return f"{Exception("Нельзя делить на ноль")}"
    else:
        return f"{a/b}"
def sqroot(a):
    """Checking for exceptions in square rooting"""
    if a >= 0:
        print(f"{math.sqrt(a)}")
    else:
        print("Из отрицательного числа квадратный корень не извлекается")
def checknumber(a):
    """Checking if a is a number"""
    status = "ok"
    try:
        number = float(a)
        print(f"Число {number} введено корректно")
    except:
        print("Это строка. Не число!")
        status = "rejected"
    return status
def tangens(a):
    """Checking for errors in calculating tg"""
    if (a % 90 == 0) and (a % 180 != 0):
        raise ArithmeticError
    try:
        print(f"Тангенс {a} равен {math.tan(math.radians(a))}")
    except ArithmeticError:
        print("Из данного числа тангенс не выводится!")
    finally:
        print("Подсчёт тангенса завершён")
def logarithm(a, b):
    """Checking for errors in counting logarithm"""
    try:
        n1 = float(a)
        n2 = float(b)
        if (n1 < 0) or (n2 < 0):
            raise ArithmeticError
        print(f"Логарифм {a} по основанию {b} равен {math.log(n1, n2)}")
    except ArithmeticError:
        print("Повторяй алгебру, дружок!")
    except ValueError:
        print("Здесь затесалась строка. Что-то ты мудришь...")
    except BaseException:
        print("Косяк случился, косяк бывает. Какой именно - думай сам")
    finally:
        print("Подсчёт логарифма окончен!")
def root(a, b):
    """Checking for errors in counting root"""
    try:
        if (a < 0) and (b % 2 == 0):
            raise ArithmeticError
        elif b == 0:
            raise TypeError
        print(f"Корень степени {b} от числа a равен {a ** (1 / b)}")
    except ValueError:
        print("Со строками нельзя вести подсчёты")
    except ArithmeticError:
        print("Из отрицательного числа нельзя получить корень чётной степени")
        print(f"Возможно, вы имели в виду корень степени {b} от числа a равен {(-1* a) ** (1 / b)}")
    except TypeError:
        print("Степень корня не должна равняться 0")
    except BaseException:
        print("Косяк случился, косяк бывает. Какой именно - думай сам")
def maximum(a):
    """Checking for errors in finding maximum in massive"""
    if a.Length < 2:
        raise ArithmeticError
    try:
        print(f"Maximum={max(a)}")
    except ValueError:
        print("Возможно, массив состоит не из чисел. Попробуйте ещё раз")
    except ArithmeticError:
        print("В массиве должно быть несколько чисел, чтобы провести сравнение")
    except BaseException as e:
        print(f"При выполнении функции произошло следующее: {e}")
def power(a, b):
    """Checking for errors in power and using *raise* operator """
    if (a == 0) or (b < 0):
        raise ArithmeticError
    try:
        print(f"{a} в степени {b} равняется {a ** b}")
    except ValueError:
        print("Похоже, вы ввели строку, а не число")
    except ArithmeticError:
        print("Введите положительное b и a, не равное 0. А то в вычислениях не будет смысла")
    finally:
        print("Возведение в степень окончено!")
class FortyTwoException(Exception):
    """User exception to not use 42 in math operations"""
    def __str__(self):
        return "Вы не можете посягать на выполнение операций с числом 42!"
class TooBigNumberException(Exception):
    """User exception to limit the number"""
    def __init__(self, limit):
        self.limit = limit
    def __str__(self):
        return f"Слишком большое число. Допустимый предел - {self.limit}"
class CtgDoesntExistException(Exception):
    """User exception for non-existing cotangens of angle"""
    def __str__(self):
        return "Для данного числа котангенса на существует"
class Coordinate():
    """Class for defining coordinate"""
    def __init__(self, x, y, limit):
        if x < limit:
            self.x = x
        else:
            raise TooBigNumberException(limit)
        if y < limit:
            self.y = y
        else:
            raise TooBigNumberException(limit)
def cot(a):
    """Checking for errors in ctg"""
    if a % 180 == 0:
        raise CtgDoesntExistException
    elif a == 42:
        raise FortyTwoException
    else:
        print(math.cos(math.radians(a))/math.sin(math.radians(a)))
def summa(a, b):
    """Checking for user exceptions"""
    if (a > 1000) or (b > 1000):
        raise TooBigNumberException(1000)
    if (a == 42) or (b == 42):
        raise FortyTwoException
    try:
        print(f"{a}+{b}={a+b}")
    except TooBigNumberException:
        print("Слишком большие числа в операциях")
    except FortyTwoException:
        print("42 не нуждается в отдельных операциях")
    finally:
        print("Суммирование закончено")
tangens(45)
