x = lambda a: a + 10
print(x(5))
y = lambda a, b, c: a * b * c
print(y(5, 6, 7))


def myfunction(n):
    return lambda a: a * n


dubler = myfunction(2)
tripler = myfunction(3)

print(dubler(11))
print(tripler(11))
