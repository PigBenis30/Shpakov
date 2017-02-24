ENDREC = "endrec."
ENDFILE = "end."
KEYTOVALUE = "=>"

def load_dbtickets(dbfile = open("dbtickets")):
    import sys
    inf = sys.stdin
    sys.stdin = dbfile
    db = {}
    key = input()
    while key != ENDFILE:
        db[eval(key)] = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(KEYTOVALUE)
            db[eval(key)][name] = eval(value)
            field = input()
        key = input()
    sys.stdin = inf
    dbfile.close()
    return db

def store_dbtickets(db, dbfile = open("dbtickets")):
    dbfile = open("dbtickets", "w")
    for key in db:
        print(key, file = dbfile)
        for (name, value) in db[key].items():
            print(name + KEYTOVALUE + repr(value), file = dbfile)
        print(ENDREC, file = dbfile)
    print(ENDFILE, file = dbfile)
    dbfile.close()


def load_db(dbfile = open("dbfile")):
    import sys
    inf = sys.stdin
    sys.stdin = dbfile
    db = {}
    key = input()
    while key != ENDFILE:
        rec = {}
        field = input()
        while field != ENDREC:

            if field == 'days':
                rec['days'] = {}
                field = input()
                while field != ENDREC:
                    rec['days'][eval(field)] = {}
                    tmp = eval(field)
                    field = input()
                    while field!= ENDREC:
                        name, value = field.split(KEYTOVALUE)
                        rec['days'][tmp][name] = eval(value)
                        field = input()
                    field = input()
                field = input()

            elif field == 'time':
                rec['time'] = {}
                field = input()
                while field!= ENDREC:
                    name, value = field.split(KEYTOVALUE)
                    rec['time'][name] = eval(value)
                    field = input()
                field = input()

            elif field == 'subpoints':
                rec['subpoints'] = {}
                field = input()
                while field != ENDREC:
                    rec['subpoints'][eval(field)] = {}
                    tmp = eval(field)
                    field = input()
                    while field!= ENDREC:
                        name, value = field.split(KEYTOVALUE)
                        rec['subpoints'][tmp][name] = eval(value)
                        field = input()
                    field = input()
                field = input()

            else:
                name, value = field.split(KEYTOVALUE)
                rec[name] = eval(value)
                field = input()

        db[eval(key)] = rec
        key = input()
    sys.stdin = inf
    dbfile.close()
    return db

def store_db(db, dbfile = open("dbfile")):
    dbfile = open("dbfile", "w")
    for key in db:
        print(repr(key), file = dbfile)
        for (name, value) in db[key].items():
            if name == 'time':
                print(name, file = dbfile)
                for (subname, subvalue) in db[key][name].items():
                    print("{0}{1}{2}".format(subname, KEYTOVALUE, repr(subvalue)), file = dbfile)
                print(ENDREC, file = dbfile)

            elif name == 'subpoints':
                print(name, file = dbfile)
                for i in range(len(db[key][name])):
                    print(repr(i), file = dbfile)
                    for (subname, subvalue) in db[key][name][i].items():
                        print("{0}{1}{2}".format(subname, KEYTOVALUE, repr(subvalue)), file = dbfile)
                    print(ENDREC, file = dbfile)
                print(ENDREC, file = dbfile)

            elif name == 'days':
                print(name, file = dbfile)
                for i in range(len(db[key][name])):
                    print(repr(i), file = dbfile)
                    for (subname, subvalue) in db[key][name][i].items():
                        print("{0}{1}{2}".format(subname, KEYTOVALUE, repr(subvalue)), file = dbfile)
                    print(ENDREC, file = dbfile)
                print(ENDREC, file = dbfile)

            else:
                print(name + KEYTOVALUE + repr(value), file = dbfile)
        print(ENDREC, file = dbfile)
    print(ENDFILE, file = dbfile)
    dbfile.close()
