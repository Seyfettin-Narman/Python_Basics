dosya1= open("kodlama.txt","w")
print("print('seyfin kodu')",file=dosya1)
dosya1.close()
dosya1=  open("kodlama.txt","r")
satir = dosya1.readline()
eval(satir)