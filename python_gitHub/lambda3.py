def fonk1(k):
    return lambda l: l * k
katla = fonk1(3)
print(katla(4))

katla=fonk1(2)
print(katla(3))