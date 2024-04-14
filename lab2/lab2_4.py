try:
    file_input = open("input4.txt", "r",  encoding="utf8")
    file_output = open("output4.txt", "w",  encoding="utf8")
except Exception as exc:
    print(exc)

list_input = []
cyrillic_lower = {(lambda c: chr(c))(i): 0 for i in range(1072, 1104)}
list_output = []

with file_input:
    for line in file_input:
        list_input = [a.lower() for a in line if a[len(a) - 1: len(a)] != "\n"]
        for letter in list_input:
            if letter in cyrillic_lower.keys():
                cyrillic_lower[letter] += 1
file_input.close()

with file_output:
    for a in sorted(cyrillic_lower.items(), key=lambda x: x[1], reverse=True):
        file_output.write(str(a[0]) + " - " + str(a[1]) + "\n")
