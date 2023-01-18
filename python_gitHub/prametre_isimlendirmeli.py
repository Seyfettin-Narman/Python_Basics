def Toplama(*topla,fazla=0):
    toplam=0
    for val in topla:
        toplam +=val + fazla
    return toplam
print(Toplama(10,20,30,40,fazla=2))