import math

def is_rigth(x):
    try:
        x = int(x)
        return 0
    except ValueError:
        print("Неверное значение. Введите заново.")
        return 1

def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

def row(x, e):
    i = 1
    n = 1
    sum_row = 0
    while math.fabs(i) > e:
        i = ((-1) ** (n - 1)) * (x ** (2 * n - 1)) / factorial(2 * n - 1)
        sum_row += i
        n += 1
    print("n, при котором сходимось ряда меньше заданного в программе e - ", n - 1)
    return sum_row

def main():
    x = ""
    e = 0.0001
    while True:
        x = input("Введите X: ")
        if is_rigth(x) == 1:
            continue
        else:
            x = int(x)
            break
    x_sin_row = row(x, e)
    print("Функция разложения - ", x_sin_row)
    print("Функция метода - ", math.sin(x))

if __name__ =="__main__":
    main()