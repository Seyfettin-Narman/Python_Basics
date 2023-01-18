class seyf_sinif:
    yazi=""
    def __init__(self,k):
        self.yazi = k
    def __del__(self):
        print("siliniyor")
sinif_nesnesi= seyf_sinif("Seyfin sınıfı")
del sinif_nesnesi