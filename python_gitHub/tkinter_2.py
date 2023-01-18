from tkinter import *
pencere = Tk()
pencere.title("Merhaba Seyfettin")
etiket=Label(pencere,text="etiket1")
etiket2=Label(pencere,text="etiket2",font=("Arial Bold",100))

etiket.grid(column=0,row=0)
etiket2.grid(column=1,row=0)

pencere.geometry('500x500')
pencere.mainloop()