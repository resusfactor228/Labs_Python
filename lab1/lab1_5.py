num = int(input())
sum_neg = 0
sum_pos = 0
while num != 0:
    if num > 0:
        sum_pos += num
    else:
        sum_neg += num
    num = int(input())
print("Сумма положительных: " + str(sum_pos) + "\n" + "Сумма отрицательных: " + str(sum_neg))
