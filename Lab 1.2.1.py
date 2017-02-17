import functools as f

def main():
    x = ""
    while True:
        x = input("Введите число из диапазона [100 - 9999], или Q чтобы выйти:")
        if x == "Q":
            return 0
        try:
            x = int(x)
        except ValueError:
            print("Неверное значение. Введите заново.")
            continue
        x = int(x)
        if x < 100 or x > 9999:
            print("Неверное значение. Введите заново.")
        else:
            break
    if x > 999:
        answer = [int(i) for i in list(str(x))]
        print(sum(answer))
    else:
        answer = [int(i) for i in list(str(x))]
        print(f.reduce(lambda z, y: z * y, answer))



if __name__ == "__main__":
    main()
