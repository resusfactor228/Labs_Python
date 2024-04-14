try:
    file_input_1 = open("input3_1.txt", "r")
    file_input_2 = open("input3_2.txt", "r")
    file_output = open("output3.txt", "w")
except Exception as exc:
    print(exc)

try:
    list_1 = []
    list_2 = []

    with file_input_1:
        for line in file_input_1:
            list_1 += [int(a) if a.isdigit() else int(a[0: len(a) - 1]) for a in line.split(" ")]
    file_input_1.close()

    with file_input_2:
        for line in file_input_2:
            list_2 += [int(a) if a.isdigit() else int(a[0: len(a) - 1]) for a in line.split(" ")]
    file_input_2.close()

    with file_output:
        file_output.write(str([a for a in set(list_1) if a in set(list_2)]))
    file_output.close()

except Exception as exc:
    print(exc)
