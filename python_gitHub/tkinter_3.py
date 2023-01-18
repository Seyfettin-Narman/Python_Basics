from tkinter import *
pencere = Tk()
pencere.title("Merhaba Seyfettin")
etiket= Label(pencere,text="etiket1")
etiket2=Label(pencere,text="etiket2",font=("Arial Bold",50))
etiket.grid(column=0,row=0)
etiket2.grid(column=1,row=0)
pencere.geometry('500x500')
buton=Button(pencere,text="Butona Tıkla")
buton.grid(column=2,row=1)
def Tiklandi():
    etiket.configure(text="Butona tıklanma gerçekleşti")

buton2=Button(pencere,text='renkli buton tıkla',bg="orange",fg="red",width=20,height=20,command=Tiklandi)
buton2.grid(column=2,row=3)
pencere.mainloop()