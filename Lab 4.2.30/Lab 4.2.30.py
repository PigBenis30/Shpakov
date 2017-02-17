def array_output(f):
    i = 0
    for row in f:
        i += 1
    data_base = [""] * i
    for n in range(i):
        data_base[n] = [""] * 3
    index = 0
    f = open("input_file")
    for line in f:
        num = 0
        for char in line:
            if char == "." or char == "\n":
                num += 1
                continue
            data_base[index][num] += char
        index += 1
    f.close()
    max_data = [0, 0, 0]
    min_data = [31, 12, 10000]
    for n in range(i):
        for it in range(3):
            data_base[n][it] = int(data_base[n][it])
    for n in range(i):
        for it in range(3):
            if data_base[n][2] > max_data[2]:
                max_data = data_base[n]
            elif data_base[n][2] < min_data[2]:
                min_data = data_base[n]
            if data_base[n][2] == max_data[2] and data_base[n][1] > max_data[1]:
                max_data = data_base[n]
            elif data_base[n][2] == min_data[2] and data_base[n][1] < min_data[1]:
                min_data = data_base[n]
            if data_base[n][2] == max_data[2] and data_base[n][1] == max_data[1] and data_base[n][0] > max_data[0]:
                max_data = data_base[n]
            elif data_base[n][2] == min_data[2] and data_base[n][1] == min_data[1] and data_base[n][0] < min_data[0]:
                min_data = data_base[n]
    string = "Biggest data: \n"
    i = 0
    for number in max_data:
        string += str(number)
        i += 1
        if i == 3:
            continue
        string += "."
    string += "\nSmallest data: \n"
    i = 0
    for number in min_data:
        string += str(number)
        i += 1
        if i == 3:
            continue
        string += "."
    f = open("output_file", "w")
    print(string, file = f)

def main():
    f = open("input_file")
    array_output(f)

if __name__ == "__main__":
    main()
