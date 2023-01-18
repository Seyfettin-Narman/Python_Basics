"""
Kullacı adı ve şifre giriş formu oluşturunuz
Kullanıcı adı ve şifre yanlış girilirse
    uyarı penceresi çıkartınız
    doğru girilirse yeni bir pencereye geçiniz
"""

import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox

class uygulama:
    GLineEdit_1 = None
    GLineEdit_2 = None
    def __init__(self, root):

        self.GLineEdit_1 = tk.Entry(root)
        self.GLineEdit_2 = tk.Entry(root)
        root.title("tanımsız")
        genislik=508
        yukseklik=370
        ekranGenisligi = root.winfo_screenwidth()
        ekranYukseligi = root.winfo_screenheight()
        strHizala = '%dx%d+%d+%d' % (genislik, yukseklik, (ekranGenisligi - genislik) / 2, (ekranYukseligi - yukseklik) / 2)
        root.geometry(strHizala)
        root.resizable(width=False, height=False)
        Getiket1=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        Getiket1["font"] = ft
        Getiket1["fg"] = "#333333"
        Getiket1["justify"] = "center"
        Getiket1["text"] = "Kullanıcı Giriş"
        Getiket1.place(x=160,y=40,width=225,height=30)
        Gbuton1=tk.Button(root)
        Gbuton1["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        Gbuton1["font"] = ft
        Gbuton1["fg"] = "#000000"
        Gbuton1["justify"] = "center"
        Gbuton1["text"] = "Giriş"
        Gbuton1.place(x=170,y=210,width=156,height=35)
        Gbuton1["command"] = self.Gbuton1_emri

        Getiket2=tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        Getiket2["font"] = ft
        Getiket2["fg"] = "#333333"
        Getiket2["justify"] = "center"
        Getiket2["text"] = "Kullanıcı Adı"
        Getiket2.place(x=150, y=100, width=70, height=25)

        Getiket3=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        Getiket3["font"] = ft
        Getiket3["fg"] = "#333333"
        Getiket3["justify"] = "center"
        Getiket3["text"] = "Parola"
        Getiket3.place(x=150, y=150,width=70, height=25)

        self.GLineEdit_2["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GLineEdit_2["font"] = ft
        self.GLineEdit_2["fg"] = "#333333"
        self.GLineEdit_2["justify"] = "center"
        self.GLineEdit_2["text"] = "Entry"
        self.GLineEdit_2.place(x=240, y=150,width=107, height=30)
        self.GLineEdit_2["show"] = "*"

        self.GLineEdit_1["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.GLineEdit_1["font"] = ft
        self.GLineEdit_1["fg"] = "#333333"
        self.GLineEdit_1["justify"] = "center"
        self.GLineEdit_1["text"] = "Entry2"
        self.GLineEdit_1.place(x=240, y=90, width=109, height=30)

    def Gbuton1_emri(self):
        kullanici_adi = self.GLineEdit_1.get()
        parola = self.GLineEdit_2.get()
        print(kullanici_adi, parola)

        if kullanici_adi == "Seyfettin Narman" and parola == "Seyf":
            root2 = tk.Tk()
            root.title("tanımsız")
            genislik = 200
            yukselik = 200
            ekranGenisligi = root.winfo_screenwidth()
            ekranYuksekligi = root.winfo_screenheight()
            strHizala = '%dx%d+%d+%d' % (genislik, yukselik, (ekranGenisligi - genislik) / 2, (ekranYuksekligi - yukselik) / 2)
            root2.geometry(strHizala)
            root2.resizable(width=False, height=False)
            root.destroy()
        else:
            tk.messagebox.showerror(title="Hata!!!", message="Yanlış kullanıcı adı ya da parola")


if __name__ == "__main__":
    root = tk.Tk()
    uygulama = uygulama(root)
    root.mainloop()