def change(string):
    str = ""
    i = 0
    while i < len(string):
        if string[i] == "ч" or string[i] == "Ч" or string[i] == "щ" or string[i] == "Щ":
            str += string[i]
            if string[i + 1] == "ю":
                str += "у"
                i += 1
        elif string[i] == "ж" or string[i] == "Ж" or string[i] == "ш" or string[i] == "Ш":
            str += string[i]
            if string[i + 1] == "ы":
                str += "и"
                i += 1
        else:
            str += string[i]
        i += 1
    return str

def is_rigth(x):
    try:
        x = int(x)
        return 0
    except ValueError:
        print("Неверное значение: ")
        return 1



def main():
    n = 0
    str = ""
    while True:
        n = input("Введите количество строк: ")
        if is_rigth(n):
            continue
        n = int(n)
        print(n)
        i = 0
        while i < n:
            i += 1
            str += "\n"
            str += input()
        iterator = 0
        while iterator < len(str):
            str = change(str)
            iterator += 1
        break
    print(str)

if __name__ == "__main__":
    main()
