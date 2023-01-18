"""
1 - veri isimli bir klasör oluşturun
2 - zip dsosyasını veri klasörüne çıkartın
3 - zip dosyası içindeki csv dosyalarının tüm içeriğini
    tek bir csv dosyasında birleştirin
    volume olmasın
4 - bu kayıtların tamamını sqlite veritabanına bir tablo
    oluşturarak yükleyin
5 - kullanıcının belirlediği paritenin
    kullanıcının belirlediği aralığının
    kullanıcının belirlediği değerin
    grafiğini çizdirin (veriler sqlite tan çekilecek).
"""


import sqlite3
import matplotlib.pyplot as plt
baglanti = sqlite3.connect("kripto.vt")
imlec = baglanti.cursor()

pariteler = "TRXUSDT"

basTarih = "2023-01-03"
bitTarih = "2023-01-04"
sorgu = "SELECT * FROM parite WHERE " \
        "(otime BETWEEN '"+basTarih+"' " \
        "AND '"+bitTarih+"') " \
        "AND parite='"+pariteler+"'"
imlec.execute(sorgu)
sonuclar = imlec.fetchall()
listeX= []
listeY = []
for mum in sonuclar:
    listeX.append(mum[7])
    listeY.append(mum[6])
plt.plot(listeX, listeY)
plt.show()
baglanti.close()