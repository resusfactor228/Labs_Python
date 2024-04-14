try:
    file_input = open("input2.txt", "r")
    file_output = open("output2.txt", "w")
except Exception as exc:
    print(exc)

try:
    mult = 1
    i = 0

    with file_input:
        line = file_input.readline()
        line = [int(a) if a.isdigit() else int(a[0: len(a) - 1]) for a in line.split(" ")]
        for a in line:
            if i != 10:
                i += 1
                mult *= a
            else:
                break
        file_input.close()

except Exception as exc:
    print(exc)

try:
    with file_output:
        file_output.write(str(mult))
    file_output.close()
except Exception as exc:
    print(exc)
