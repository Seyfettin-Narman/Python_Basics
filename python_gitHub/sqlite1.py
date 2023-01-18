import sqlite3

baglanti = sqlite3.connect("seyf.vt")
imlec = baglanti.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS personel "
               "(id INTEGER NOT NULL PRIMARY KEY,"
               "isim TEXT, soyisim TEXT, bolum TEXT, "
               "calıstıgı_gun_sayisi INT)")
baglanti.commit()
baglanti.close()