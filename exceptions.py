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
    except ValueError:
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
tangens(45)
