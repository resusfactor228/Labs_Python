def hofstadter_f_m(n):
    f, m = [1], [0]  # Начальные значения последовательностей F и M
    print("n = 1")
    print("Result:")
    print((f[0], m[0]), "\n")

    for j in range(1, n):
        m.append(j - f[m[j - 1]])
        f.append(j - m[f[j - 1]])
        yield f[j], m[j]


print("Input your N: ")
n = int(input())
print("\n")

list_ = hofstadter_f_m(n)
for i in range(1, n):
    if list_ == StopIteration:
        break
    res = next(list_)
    print(f"n = {i + 1}")
    print("Result:")
    print(res, "\n")
