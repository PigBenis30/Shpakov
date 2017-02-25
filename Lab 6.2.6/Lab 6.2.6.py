import DataBase
import sys
import os

def __doc__():
    """Данная программа предназначена для учебных целей.
    Она не может учитывать невероятнео множество факторов,
    которые требуют контроля людей, однако поставленные перед собой
    задачи, дополняя их встроенной базой данных, выполняет"""

def plane_info(db_tickets, db_planes):
    while True:
        cls()
        print("Номера рейсов:")
        for i in range(len(db_planes)):
            print("{0}.Рейс номер {1} ({2})".format(i, db_planes[i]['number'], db_planes[i]['country']))
        print("Введите номер рейса:")
        number = int_input()
        id = -1
        for i in range(len(db_planes)):
            if number == db_planes[i]['number']:
                id = i
        if id != -1:
            counter = 0
            capacity = 0
            for i in range(len(db_tickets)):
                if db_tickets[i]['plane'] == number:
                    capacity += 1
            print_plane(db_planes[id])
            print("Людей, забронировавших данный рейс - {0}".format(capacity))
            break
        else:
            continue

def search_path(db):
    while True:
        cls()
        for i in range(len(db)):
            print("{0}.{1}".format(i, db[i]['country']))
            for j in range(len(db[i]['subpoints'])):
                if db[i]['subpoints'][j]['country'] != "":
                    print("    {0}.{1}".format(j, db[i]['subpoints'][j]['country']))
        print("Введите название страны: ")
        country = char_input()
        length = 40000
        number = 0
        for i in range(len(db)):
            if country == db[i]['country'] and db[i]['length'] < length:
                length = db[i]['length']
                number = db[i]['number']
            for j in range(len(db[i]['subpoints'])):
                if country == db[i]['subpoints'][j]['country'] and sum([db[i]['subpoints'][it]['length'] for it in range(len(db[i]['subpoints']))]) < length:
                    length = sum([db[i]['subpoints'][it]['length'] for it in range(len(db[i]['subpoints']))])
                    number = db[i]['number']
        if length != 40000:
            print("Ваш подходящий рейс - {0}. Расстояние - {1}".format(number, length))
            input("Введите любую строку для продолжения...")
            break

def print_ticket(db, db_plane):
    print("Введите ваш номер паспорта:")
    iterator = -1
    plane_id = -1
    while True:
        print("Введите первые две буквы номера паспорта:")
        id = char_input()
        if len(id) != 2:
            print("Неверные данные")
            continue
        print("Введите номер паспорта (семизначный):")
        number = int_input()
        if len([int(i) for i in str(number)]) != 7:
            print("Неверные данные")
            continue
        for i in range(len(db)):
            if db[i]['id'] == id and db[i]['number'] == number:
                iterator = i
                plane_id = db[i]['plane']
                break
        if iterator != -1:
            for i in range(len(db_plane)):
                if db_plane[i]['number'] == plane_id:
                    plane_id = i
                    break
            print_plane(db_plane[plane_id])
            print("Ф.И.О - {0} {1} {2}, Номер паспорта - {3}{4}".format(db[iterator]['lastname'], db[iterator]['name'], db[iterator]['subname'], db[iterator]['id'], db[iterator]['number']))
            break
        else:
            case = 0
            while True:
                print("Не найден билет. Выйти? 1.Да 2.Нет")
                switch = input()
                if switch == "1":
                    case = 1
                    break
                elif switch == "2":
                    case = 2
                    break
                else:
                    print("Неверное значение")
            if case == 1:
                break
            elif case == 2:
                continue

def check_passport(counter, db, id, number):
    for i in range(counter):
        if db[i]['id'] == id and db[i]['number'] == number:
            return 0
    return 1

def del_ticket(db):
    while True:
        iterator = -1
        cls()
        print("Выберите пункт меню:\n1.Отдать билет\n2.Назад")
        switch = input()
        if switch == "1":
            while True:
                print("Введите первые две буквы номера паспорта:")
                id = char_input()
                if len(id) != 2:
                    print("Неверные данные")
                    continue
                print("Введите номер паспорта (семизначный):")
                number = int_input()
                if len([int(i) for i in str(number)]) != 7:
                    print("Неверные данные")
                    continue
                for i in range(len(db)):
                    if db[i]['id'] == id and db[i]['number'] == number:
                        iterator = i
                        break
                if iterator != -1:
                    db[iterator], db[len(db) - 1] = db[len(db) - 1], db[iterator]
                    db.pop(len(db) - 1)
                    break
                else:
                    print("Билет не найден")
                    continue
        elif switch == "2":
            break

def add_ticket(db, db_plane):
    counter = len(db)
    db[counter] = {}
    print("Введите Ваше имя: ")
    db[counter]['name'] = char_input()
    print("Введите Вашу фамилию: ")
    db[counter]['lastname'] = char_input()
    print("Введите Ваше отчество: ")
    db[counter]['subname'] = char_input()
    while True:
        while True:
            print("Введите первые две буквы паспорта: ")
            db[counter]['id'] = char_input()
            if len(db[counter]['id']) > 2:
                print("Неверное значение")
                continue
            break
        while True:
            print("Введите номер паспорта (семизначный)")
            db[counter]['number'] = int_input()
            if len([int(i) for i in str(db[counter]['number'])]) != 7:
                print("Неверное значение")
                continue
            break
        it = counter - 1
        if check_passport(it, db, db[counter]['id'], db[counter]['number']) == 0:
                print("Такой номер паспорта уже зарегистрирован")
        else:
            break
    while True:
        print("Номера рейсов:")
        for i in range(len(db_plane)):
            print("{0}.Рейс номер {1} ({2})".format(i, db_plane[i]['number'], db_plane[i]['country']))
        print("Введите номер рейса: ")
        db[counter]['plane'] = int_input()
        id = -1
        for i in range(len(db_plane)):
            if db_plane[i]['number'] == db[counter]['plane']:
                id = i
        if id != -1:
            print("Рейс найден")
            capacity = 0
            if db_plane[id]['type'] == 'Ty-154':
                limit = 140
            else:
                limit = 80
            for i in range(len(db)):
                if db[i]['plane'] == db[counter]['plane']:
                    capacity += 1
            if limit - capacity > 0:
                print("Рейс забронирован")
                break
            else:
                print("Нету свободных мест")
        else:
            print("Рейс не найден")
    return db

def tickets_func(db, db_plane):
    while True:
        cls()
        print("=====================\n1.Заказать билет\n2.Вернуть билет\n0.Выйти из подменю\n=====================\nВыберите пункт в меню: ")
        switch = input()
        if switch == "1":
            add_ticket(db, db_plane)
        elif switch == "2":
            del_ticket(db)
        elif switch == "0":
            break
    return db

def delete_plane(db):
    while True:
        cls()
        print("1.Удалить рейс\n 2.Назад")
        switch = input()
        if switch == "1":
            print("Введите номер удаляемого рейса: ")
            check = 0
            number = int_input()
            for i in range(len(db)):
                if number == db[i]['number']:
                    print("Рейс удален ")
                    temp = db[len(db) - 1]
                    db[len(db) - 1] = db[i]
                    db[i] = temp
                    db.pop(len(db) - 1)
                    check = 1
                    break
            if check == 0:
                print("Рейс не найден")
        elif switch == "2":
            break

def search_date(db):
    check = 0
    while True:
        print("Введите дату:\nВведите день")
        day = int_input()
        if day < 0 or day > 31:
            print("Неверное знаениче. Введите заново")
            continue
        print("Введите месяц")
        mounth = int_input()
        if mounth < 0 or mounth > 12:
            print("Неверное знаениче. Введите заново")
            continue
        break
    for i in range(len(db)):
        for j in range(len(db[i]['days'])):
            if db[i]['days'][j]['day'] == day and db[i]['days'][j]['mounth'] == mounth:
                print_plane(db[i])
                check = 1
    if check == 0:
        print("Рейс не найден")

def search_country(db):
    check = 0
    print("Введите страну: ")
    country = char_input()
    for i in range(len(db)):
        if db[i]['country'] == country:
            print("Страна найдена: ")
            print_plane(db[i])
            check = 1
    if check == 0:
        for i in range(len(db)):
            for j in range(len(db[i]['subpoints'])):
                if db[i]['subpoints'][j]['country'] == country:
                    print("Страна найдена: ")
                    print_plane(db[i])
                    check = 1
    if check == 0:
        print("Рейс не найден")


def search_type(db):
    while True:
        print("Выберите тип самолета:\n1.Boing\n2.Ty-154")
        switch = input()
        if switch == "1":
            sub_processing(db, 'Boing')
            break
        elif switch == "2":
            sub_processing(db, 'Ty-154')
            break
        else:
            print("Неверно введенные данные ")

def sub_processing(db, str):
    check = 0
    for i in range(len(db)):
        if db[i]['type'] == str:
            check = 1
            print_plane(db[i])
    if check == 0:
        print("Рейс не найден")


def search_number(db):
    check = 0
    print("Введите номер рейса: ")
    temp = int_input()
    for i in range(len(db)):
        if temp == db[i]['number']:
            print("Рейс найден: ")
            print_plane(db[i])
            check = 1
    if check == 0:
        print("Рейс не найден")

def search_plane(db):
    while True:
        cls()
        print("=====================\nПоиск по полю.\n1.По рейсу\n2.По типу самолета\n3.По стране\n4.По дате\n0.Выход из подменю\n=====================")
        switch = input("Введите пункт в меню: ")
        if switch == "1":
            search_number(db)
        elif switch == "2":
            search_type(db)
        elif switch == "3":
            search_country(db)
        elif switch == "4":
            search_date(db)
        elif switch == "0":
            break
        else:
            pass

def print_plane(db_current_element):
    print("=====================")
    print("Номер рейса - ", db_current_element['number'])
    print("Пункт назначения - {0}, расстояние - {1} км".format(db_current_element['country'], db_current_element['length']))
    print("Тип самолета - ", db_current_element['type'])
    if db_current_element['subpoints'][0]['country'] == '':
        print("Дополнительные пункты: - ")
    else:
        print("Дополнительные пункты: ")
        for it in range(len(db_current_element['subpoints'])):
            if db_current_element['subpoints'][it]['country'] != "":
                print("Страна - {0}, расстояние от предыдущего пункта - {1} км".format(db_current_element['subpoints'][it]['country'], db_current_element['subpoints'][it]['length']))
    format_time(db_current_element['time']['hours'], db_current_element['time']['minutes'])
    for it in range(len(db_current_element['days'])):
        format_days(db_current_element['days'][it]['day'], db_current_element['days'][it]['mounth'])

def print_planes(db):
    if len(db) == 0:
        print("Отстутствуют рейсы.")
        return
    for i in range(len(db)):
        print_plane(db[i])
    input("Введите любую строку...")
    cls()

def format_time(hours, minutes):
    if hours < 10 and minutes < 10:
        print("Время - 0{0}.0{1}".format(hours, minutes))
    elif hours < 10:
        print("Время - 0{0}.{1}".format(hours, minutes))
    elif minutes < 10:
        print("Время - {0}.0{1}".format(hours, minutes))
    else:
        print("Время - {0}.{1}".format(hours, minutes))

def format_days(day, mounth):
    if day < 10 and mounth < 10:
        print("Отправка рейса будет произведена 0{0}.0{1}".format(day, mounth))
    elif day < 10:
        print("Отправка рейса будет произведена - 0{0}.{1}".format(day, mounth))
    elif mounth < 10:
        print("Отправка рейса будет произведена - {0}.0{1}".format(day, mounth))
    else:
        print("Отправка рейса будет произведена - {0}.{1}".format(day, mounth))

def time_input():
    time = {}
    print("Введите время: ")
    while True:
        print("Введите часы: ")
        time['hours'] = int_input()
        if time['hours'] < 0 or time['hours'] > 24:
            cls()
            print("Неверное значение, введите заного:")
        else:
            break
    while True:
        print("Введите минуты: ")
        time['minutes'] = int_input()
        if time['minutes'] < 0 or time['minutes'] > 60:
            cls()
            print("Неверное значение, введите заного:")
        else:
            break
    return time

def days_input():
    i = 0
    days = {}
    while True:
        print("Введите количество вводимых дней:")
        n = int_input()
        if n < 1:
            print("Неверное значение")
        else:
            break
    while i < n:
        print("Введите дату: ")
        days[i] = {}
        while True:
            print("Введите день: ")
            days[i]['day'] = int_input()
            if days[i]['day'] < 0 or days[i]['day'] > 31:
                cls()
                print("Неверное значение, введите заново:")
            else:
                break
        while True:
            print("Введите месяц:")
            days[i]['mounth'] = int_input()
            if days[i]['mounth'] < 0 or days[i]['mounth'] > 12:
                cls()
                print("Неверное значение, введите заново:")
            else:
                break
        i += 1
    return days

def int_input():
    while True:
        x = input()
        try:
            x = int(x)
            return x
        except ValueError:
            print("Неверное значение, введите заново:")

def char_input():
    while True:
        x = input()
        try:
            x = int(x)
            print("Неверное значение, введите заново:")
        except ValueError:
            return x

def add_plane(db):
    cls()
    counter = len(db)
    db[counter] = {}
    print("Введите номер рейса:")
    while True:
        db[counter]['number']= int_input()
        check_val = 0
        for it in range(len(db) - 1):
            if db[counter]['number'] == db[it]['number']:
                print("Неверный номер. Такой рейс уже есть. Введите заново:")
                check_val = 1
        if check_val != 1:
            break
    cls()
    while True:
        print("Выберите тип самолета:\n1.Boing\n2.Ty-154")
        switch = input()
        if switch == "1":
            db[counter]['type'] = "Boing"
            break
        elif switch == "2":
            db[counter]['type'] = "Ty-154"
            break
        else:
            print("Неверно введенные данные ")
        cls()
    cls()
    print("Введите название страны, в которую будет совершена посадка")
    db[counter]['country'] = char_input()
    cls()
    while True:
        print("Введите расстояние из Беларуси в пункт назначения (км)")
        db[counter]['length'] = int_input()
        if db[counter]['length'] > 40000 or db[counter]['length'] < 100:
            print("Неверно введенные данные")
        else:
            break
    cls()
    db[counter]['subpoints'] = {}
    i = 0
    while True:
        cls()
        print("Введите дополнительные пункты посадки. Введите q чтобы выйти из этого меню.\nВведите страну:")
        db[counter]['subpoints'][i] = {}
        db[counter]['subpoints'][i]['country'] = char_input()
        if db[counter]['subpoints'][i]['country'] == "q":
            db[counter]['subpoints'][i]['country'] = ""
            db[counter]['subpoints'][i]['length'] = 0
            break
        check_val = 0
        for it in range(len(db)):
            if db[it]['country'] == db[counter]['subpoints'][i]['country']:
                print("Неверные данные. Такая страна уже есть")
                check_val = 1
                break
        if check_val == 1:
            print("Остановка ввода поля...")
            break
        print("Введите расстояние: ")
        sum = 0
        while True:
            db[counter]['subpoints'][i]['length'] = int_input()
            for it in range(i):
                sum += db[counter]['subpoints'][it]['length']
            if sum > db[counter]['length'] - 50 or db[counter]['subpoints'][i]['length'] < 50:
                print("Неверные данные. Введите число заново:")
            else:
                break
        if sum > db[counter]['subpoints'][i]['length'] - 100:
            print("Остановка ввода поля...")
            break
        i += 1
    db[counter]['time'] = time_input()
    db[counter]['days'] = days_input()
    return db

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    db = DataBase.load_db()
    db_tickets = DataBase.load_dbtickets()
    while True:
        cls()
        print("=====================\n1.Добавить рейс в базу данных\n2.Поиск рейса по данным\n3.Ближайший рейс до существующих пунктов\n4.Заказ или отмена билетов\n5.Печать билета\n6.Посадочная ведомость рейса\n7.Вывод рейсов.\n8.Удаление рейса\n0.Выход\n=====================")
        switch = input("Введите пункт меню: ")
        if switch == "1":
            db = add_plane(db)
        elif switch == "2":
            search_plane(db)
        elif switch == "3":
            search_path(db)
        elif switch == "4":
            tickets_func(db_tickets, db)
        elif switch == "5":
            print_ticket(db_tickets, db)
        elif switch == "6":
            plane_info(db_tickets, db)
        elif switch == "7":
            print_planes(db)
        elif switch == "8":
            delete_plane(db)
        elif switch == "0":
            break
        else:
            print("Неверно введенные данные.")
    DataBase.store_db(db)
    DataBase.store_dbtickets(db_tickets)

if __name__ == "__main__":
    main()
