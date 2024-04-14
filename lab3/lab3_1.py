def cross(*lists):
    list_ = set(lists[0])
    for i in range(1, len(lists)):
        list_ = set(lists[i]) & list_
    return list_


print(list(cross([1, 2, 3], [1, 3, 5], [2, 3, 5])))
