def verilenleri_topla(*k):
    toplam=0
    for val in k:
        toplam +=val
    return toplam
print(verilenleri_topla(10,20,30,10.5,15,2))