from tkinter import *
import pyautogui
pencere = Tk()
pencere.title("Merhaba Seyfettin")
etiket = Label(pencere,text="etiket1")
etiket2 = Label(pencere,text="etiket2",font=("Arial Bold",20))
etiket.grid(column=1,row=0)
etiket2.grid(column=1,row=0)
pencere.geometry('500x500')
buton = Button(pencere,text="Butona Tıkla")
buton.grid(column=1,row=1)

def Tiklandi():
    pyautogui.moveTo(200,200,duration=1,tween=pyautogui.easeInOutQuad)
buton2= Button(pencere,text="Renkli Butona Tıkla",bg="orange",fg="red",width=20,height=20,command=Tiklandi)
buton2.grid(column=1,row=3)
pencere.mainloop()
