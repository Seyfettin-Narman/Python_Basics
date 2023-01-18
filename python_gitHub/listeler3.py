dizi=["Ali","Veli","Ahmet"]
dizi.sort()
print(dizi)
dizi.reverse()
print(dizi)
def fonk(n):
    return abs(n-50)
sayi_dizisi=[100,23,64,23]
sayi_dizisi.sort(key=fonk)
print(sayi_dizisi)