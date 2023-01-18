
from tkinter import *

import variable as variable
from cryptocmd import CmcScraper
import matplotlib.pyplot as plt


from tkcalendar import DateEntry
pencere = Tk()
pencere.geometry('500x400')

etiket = Label(pencere, text="Parite")
etiket.grid(column=0, row=0)
tarihBaslangic = StringVar()
tarihBitis = StringVar()

etiket2 = Label(pencere, text="Başlangıç Tarihi")
etiket2.grid(column=0, row=1)
takvim=DateEntry(pencere, selectmode='day',
textvariable=tarihBaslangic,
date_pattern='dd-mm-yyyy')
takvim.grid(row=1, column=1, padx=15)

etiket3 = Label(pencere, text="Bitiş Tarihi")
etiket3.grid(column=0, row=2)
takvim2=DateEntry(pencere, selectmode='day',
textvariable=tarihBitis,
date_pattern='dd-mm-yyyy')
takvim2.grid(row=2, column=1, padx=15)

def Tiklandi():
    parite = variable.get()
    tarihBasla = tarihBaslangic.get()
    tarihBit = tarihBitis.get()
    scraper = CmcScraper(parite,tarihBasla,tarihBit)
    baslıklar, veriler = scraper.get_data()
    tarihVerisi = []
    kapanisDegeri = []
    hareketliOrtalama = []
    for i, veri in enumerate(veriler):
        tarihVerisi.append(veri[0])
        kapanisDegeri.append(veri[4])
        if i > 4:
            ortalama = kapanisDegeri[i] + kapanisDegeri[i - 1]
            ortalama += kapanisDegeri[i - 2] + kapanisDegeri[i - 3]
            ortalama += kapanisDegeri[i - 4]
            hareketliOrtalama.append(ortalama / 5)
        hareketliOrtalama.append(0)
        hareketliOrtalama.append(0)
        hareketliOrtalama.append(0)
        hareketliOrtalama.append(0)
        hareketliOrtalama.reverse()
        hareketliOrtalama.reverse()
        hareketliOrtalama.reverse()
        plt.plot(tarihVerisi, kapanisDegeri)
        plt.plot(hareketliOrtalama)
        plt.show()
        pass



btn2 = Button(pencere, text="Grafik Çiz",bg="pink", fg="red",command=Tiklandi)
btn2.grid(column=1, row=3)
variable = StringVar(pencere)
variable.set("BTC")


secenek = ["BTC", "ETH", "TRX"]
secenekKutusu = OptionMenu(pencere,variable,*secenek)
secenekKutusu.grid(column=1, row=0)

pencere.mainloop()