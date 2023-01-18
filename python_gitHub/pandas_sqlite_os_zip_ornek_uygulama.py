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

import zipfile
import sqlite3
import pandas as pd
import os

baglanti = sqlite3.connect("kripto.vt")

imlec = baglanti.cursor()

if not os.path.exists("veri"):
    os.mkdir('veri')
    arsivler = zipfile.ZipFile('pariteler_cikti_1hour_2022_2022.zip')
    arsivler.extractall("veri/")
    butun_dosyalar = os.listdir("veri")
    pandasCsvListesi = []
    for csv_dosya in butun_dosyalar:
        veri = pd.read_csv("veri/" + csv_dosya)
        del veri["volume"]
        veri["parite"] = csv_dosya.split("_")[0]
        pandasCsvListesi.append(veri)

    birlesmisCsvler = pd.concat(pandasCsvListesi)
    birlesmisCsvler.to_csv('hepsi.csv', index=False)
    imlec.execute("CREATE TABLE IF NOT EXISTS parite("
                +"id INTEGER PRIMARY KEY AUTOINCREMENT,"
                +"parite TEXT, otime TEXT, open FLOAT, "
                +"high FLOAT, low FLOAT, close FLOAT);")

    kayitlar = pd.read_csv("hepsi.csv")
    for satir in kayitlar.itertuples():
        imlec.execute("INSERT INTO "
                    + "parite(parite,otime,open,high,low,close)"
                    + " VALUES("
                    + "'"+satir.parite+"',"
                    + "'"+satir.otime+"',"
                    + ""+str(satir.open)+","
                    + ""+str(satir.high)+","
                    + ""+str(satir.low)+","
                    + ""+str(satir.close)+")")
    baglanti.commit()

pariteler = input("Parite Giriniz :")

basTarih = input("Başlangıç Tarihini Giriniz :")

bitTarih = input("Bitiş Tarihini Giriniz :")

sorgu = "SELECT * FROM parite WHERE " \
        "(otime BETWEEN '"+basTarih+"' " \
        "AND '"+bitTarih+"') " \
        "AND parite='"+pariteler+"'"
imlec.execute(sorgu)
sonuc = imlec.fetchall()
print(sonuc)
baglanti.close()