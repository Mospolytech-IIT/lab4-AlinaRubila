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
    except: #чтобы этот блок не выдавал предупреждение, необходимо указать тип ошибки
        print("Это строка. Не число!")
        status = "rejected"
    return status
def tangens(a):
    """Checking for errors in calculating tg"""
    try:
        print(f"Тангенс {a} равен {math.tan(math.radians(a))}")
    except:
        print("Из данного числа тангенс не выводится!")
    finally:
        print("Подсчёт тангенса завершён")
def logariphm(a, b):
    try:
        n1 = float(a)
        n2 = float(b)
        print(f"Логарифм {a} по основанию {b} равен {math.log(n1, n2)}")
    except ArithmeticError:
        print("Повторяй алгебру, дружок!")
    except ValueError:
        print("Здесь затесалась строка. Что-то ты мудришь...")
    except BaseException:
        print("Косяк случился, косяк бывает. Какой именно - думай сам")
    finally:
        print("Подсчёт логарифма окончен!")

tangens(45)
