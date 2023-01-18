"""
kendisine gönderilen sayılardan sadece palindrom
olanları toplayan
diğerlerini de bu toplamdan çıkaran ve geri
döndüren python fonksiyonunu yazınız.
"""

def polindram(*sayilar):
    toplam=0
    for sayi in sayilar:
        if str(sayi) == str(sayi)[::-1]:
            toplam += sayi
        else:
            toplam -= sayi

    return toplam
print(polindram(22,10,99,1010,1001,100001))