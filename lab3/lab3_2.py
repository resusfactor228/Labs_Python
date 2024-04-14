def reducer(m, n):
    if m >= n or m <= 0 or n <= 0:
        return "ERROR"

    for i in range(2, m):
        while n % i == 0 and m % i == 0:
            n = n // i
            m = m // i

    return m, n


print(reducer(20, 100))
