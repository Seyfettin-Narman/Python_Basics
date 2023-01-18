import sqlite3
from flask import Flask
from flask import jsonify
import json
uygulama= Flask(__name__)
@uygulama.route("/Getir")
def Getir():
    baglanti=sqlite3.connect("kripto.vt")
    imlec=baglanti.cursor()
    sorgu="SELECT * FROM parite WHERE " \
            "(otime BETWEEN '2023-01-03' " \
            "AND '2023-01-04')"\
            "AND parite='TRXUSDT'"
    imlec.execute(sorgu)
    sonuc=imlec.fetchall()
    baglanti.close()
    return sonuc
@uygulama.route("/saglamGetir/<parite>/<tarih1>/<tarih2>")
def saglamGetir(parite,tarih1,tarih2):
    baglanti = sqlite3.connect("kripto.vt")
    imlec=baglanti.cursor()
    sorgu="SELECT * FROM parite WHERE "\
            "(otime BETWEEN ' "+tarih1+"' "\
            "AND '"+tarih2+"') "\
            "AND parite='"+parite+"'"
    imlec.execute(sorgu)
    sonuc=imlec.fetchall()
    baglanti.close()
    return json.dumps(sonuc)
if __name__ == "__main__":
    uygulama.run(debug=True,host="localhost",port=22222)