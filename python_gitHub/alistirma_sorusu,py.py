"""
1 - Klavyeden girilen 3 tane sayıyı bir listeye atarak
    bunların karelerinden 50 çıktığında ortaya çıkan sonuca
    göre sıralayan
    ve listeyi buna göre yazdıran programı yazınız.
"""
sayilar = []
for i in range(0,3):
    print("{}.sayıyı giriniz".format(i+1))
    sayilar.append(eval(input()))
def siralama(n):
    return n*n-50

sayilar.sort(key=siralama)
print(sayilar)