class seyf_sinif:
    yazi=""
    def __init__(self,k):
        self.yazi=k
    def __str__(self):
        return "yazılacak yazı : " + self.yazi
sinif_nesnesi=seyf_sinif("Seyff2000")
print(sinif_nesnesi)