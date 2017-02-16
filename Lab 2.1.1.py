import os
import math
import msvcrt as m

def radius(x):
    value = x / 2 / math.sqrt(6)
    print("Радиус шара, вписанного в тэтраэдр - ", value)
    wait()

def volume(x):
    value = math.sqrt(3) * x / 4
    value *= 1 / 3 * x * math.sqrt(6) / 3
    print("Объем тэтраэдра - ", value)
    wait()

def hight(x):
    value = x * math.sqrt(6) / 3
    print("Высота - ", value)
    wait()

def wait():
    print("Нажмите любую клавишу чтобы продолжить...")
    m.getch()

def squere(x):
    value = math.sqrt(3) * x / 4
    "Площадь грани - {0}, площадь поверхности - {1}".format(value, value * 4)
    wait()

def sum_length(x):
    print("Сумма сторон - ", x * 6)
    wait()

def is_rigth(x):
    try:
        x = int(x)
        return 0
    except ValueError:
        print("Неверное значение. Введите заново.")
        cls()
        return 1

def init_func():
    x = ""
    while True:
        cls()
        x = input("Введите сторону тэтраэдра\n")
        if is_rigth(x) == 1:
            print("Не верное значение")
            wait()
            continue
        else:
            wait()
            return int(x)

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    typed = False
    while True:
        x = ""
        cls()
        x = input("1.Ввод длянны тэтраэдра.\n2.Вывод общей длины всех ребер тэтраэдра\n3.Вывод площади всех граней тэтраэдра\n4.Вывод объема тэтраэдра\n5.Вывод высоты тэтраэдра\n6.Вывод радиуса вписанного шара\n7.Версия программы и автор\n8.Выход\n")
        if is_rigth(x) == 1:
            print("Не верное значение")
            wait()
            continue
        x = int(x)
        if x < 1 or x > 8:
            print("Неверное значение. Введите заново.")
            cls()
        else:
            if x == 1:
                length = init_func()
                typed = True
            elif x == 2:
                if typed:
                    sum_length(length)
                else:
                    print("Не введены стороны")
                    wait()
                    continue
            elif x == 3:
                if typed:
                    squere(length)
                else:
                    print("Не введены стороны")
                    wait()
                    continue
            elif x == 4:
                if typed:
                    volume(length)
                else:
                    print("Не введены стороны")
                    wait()
                    continue
            elif x == 5:
                if typed:
                    hight(length)
                else:
                    print("Не введены стороны")
                    wait()
                    continue
            elif x == 6:
                if typed:
                    radius(length)
                else:
                    print("Не введены стороны")
                    wait()
                    continue
            elif x == 7:
                print("==================\nAuthor: Никита Шпаков \nVersion: 1.0 \n==================")
                wait()
            else:
                return 0



if __name__ == "__main__":
    main()