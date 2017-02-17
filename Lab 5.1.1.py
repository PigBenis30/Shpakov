import random

def print_deque(deque, l):
    for i in range(l):
        print(deque[i])

def is_rigth(x):
    try:
        x = int(x)
        return 0
    except ValueError:
        print("Неверное значение: ")
        return 1

def steck(length):
    steck = []
    letters = "qwertyuiopasdfghjklzxcvbnm"
    for i in range(length):
        steck.append(random.choice(letters))
    return steck

def main():
    n = ""
    l = ""
    while True:
        n = input("Введите размерность массива: ")
        if is_rigth(n):
            continue
        n = int(n)
        l = input("Введите размерность стека: ")
        if is_rigth(l):
            continue
        l = int(l)
        deque = [""] * n
        for i in range(n):
            deque[i] = steck(l)
        print_deque(deque, n)
        print("\nОтсортированные стеки:\n")
        for i in range(n):
            deque[i].sort()
        print_deque(deque, n)
        print("\nОтсортированный соединенный стек:\n")
        big_steck = []
        for i in range(n):
            big_steck += deque[i]
        big_steck.sort()
        print(big_steck)
        break


if __name__ == "__main__":
    main()