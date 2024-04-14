line = str(input())
line_ = [line[0] + "."]

for i in range(0, len(line) - 1):
    if (line[i] == " ") & (line[i+1] != " "):
        line_.append(line[i + 1] + ".")

print(line_[0] + line_[1])
