import math

try:
    file_input = open("input1.txt", "r")
    file_output = open("output1.txt", "w")
except Exception as exc:
    print(exc)

try:
    min_value = math.inf
    max_value = 0

    with file_input:
        for line in file_input:
            line = [int(a) if a.isdigit() else int(a[0: len(a) - 1]) for a in line.split(" ")]
            print(line)
            min_value = min(line) if min(line) < min_value else min_value
            max_value = max(line) if max(line) > max_value else max_value
    file_input.close()
except Exception as exc:
    print(exc)

try:
    with file_output:
        file_output.write(str(max_value) + " " + str(min_value))
    file_output.close()
except Exception as exc:
    print(exc)
