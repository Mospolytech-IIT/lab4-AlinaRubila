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
    try:
        if (a % 90 == 0) and (a % 180 != 0):
            raise ArithmeticError
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
def maximum(a):
    """Checking for errors in finding maximum in massive"""
    try:
        if len(a) < 2:
            raise ArithmeticError
        print(f"Maximum={max(a)}")
    except ValueError:
        print("Возможно, массив состоит не из чисел. Попробуйте ещё раз")
    except ArithmeticError:
        print("В массиве должно быть несколько чисел, чтобы провести сравнение")
    except BaseException as e:
        print(f"При выполнении функции произошло следующее: {e}")
def power(a, b):
    """Checking for errors in power and using *raise* operator """
    try:
        if (a == 0) or (b < 0):
            raise ArithmeticError
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
    try:
        if a % 180 == 0:
            raise CtgDoesntExistException
        elif a == 42:
            raise FortyTwoException
        else:
            print(f"Котангенс равен={math.cos(math.radians(a))/math.sin(math.radians(a))}")
    except CtgDoesntExistException as e:
        print(e)
    except FortyTwoException as e:
        print(e)
def summa(a, b):
    """Checking for user exceptions"""
    try:
        if (a > 1000) or (b > 1000):
            raise TooBigNumberException(1000)
        if (a == 42) or (b == 42):
            raise FortyTwoException
        print(f"{a}+{b}={a+b}")
    except TooBigNumberException:
        print("Слишком большие числа в операциях")
    except FortyTwoException:
        print("42 не нуждается в отдельных операциях")
    finally:
        print("Суммирование закончено")
def difference(a, b):
    """Usage of exceptions vol. 1"""
    found_diff = True
    try:
        diff = abs(float(a)-float(b))
        if diff > 10:
            raise TooBigNumberException(10)
    except TooBigNumberException:
        print("Разница слишком большая")
        found_diff = False
    except ValueError:
        print("Возможно, вы пытались выполнить операцию со строками")
        found_diff = False
    finally:
        print(f"Нашли ли разницу: {found_diff}")
def minint(a, b, c):
    """Usage of exceptions vol. 2"""
    result = 0
    try:
        if (a % round(a) != 0) or (b % round(b) != 0) or (c % round(c) != 0):
            raise ValueError
        else:
            result = min(a, b, c)
    except ValueError as e:
        print(f"Одно или несколько из чисел не являются целыми! ({e})")
    return result
def find42(a):
    """Usage of exceptions vol. 3"""
    l = len(a)
    try:
        for i in range(0, l):
            if a[i] == 42:
                raise FortyTwoException
        print("Массив проверен - 42 нет!")
    except FortyTwoException:
        print("Число 42 в массиве было найдено!")
        for i in range(0, l):
            if a[i] == 42:
                print(f"Номер этого элемента: {i}")
    finally:
        print("Проверка окончена!")
def allfuncs():
    """All the functions"""
    division(23, 0)
    division(23, 2)
    sqroot(-25)
    sqroot(25)
    print(checknumber("hello"))
    print(checknumber(12))
    tangens(90)
    tangens(45)
    logarithm("hi", 12)
    logarithm(-10, 10)
    logarithm(100, 10)
    root(-10, 4)
    root(10, 0)
    root(1000, 3)
    maximum([23])
    maximum([23, 'ki', 45])
    maximum([34, 900, 87, 99])
    power(18, -2)
    power(18, 2)
    cot(180)
    cot(42)
    cot(45)
    summa(1200, 99)
    summa(90, 90)
    difference(100, 65)
    difference(8, 5)
    print(minint(12.6, 90, 8))
    print(minint(123, 45, 6))
    find42([34, 45, 42, 90])
    find42([34, 67, 90])
if __name__ == "__main__":
    allfuncs()
