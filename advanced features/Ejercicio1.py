def primos(maximo):
    for i in range(maximo):
        if (i <= 7):
            if (i == 2) or (i == 3) or (i == 5) or (i == 7):
                yield i
        else:
            if (i%2 != 0) and (i%3 != 0) and (i%5 != 0) and (i%7 != 0):
                yield i

maximo = 100
for i in primos(maximo):
    print(i)