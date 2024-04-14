print("Введите N")
n = int(input())
vec = []
for i in range(n):
    print("Осталось ввести: " + str(n - i))
    string = str(input())
    vec.append(string)
vec_ = [a for a in vec if vec.count(a) == 1]
print(vec_)
