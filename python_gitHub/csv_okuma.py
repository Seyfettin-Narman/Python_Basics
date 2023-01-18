import csv


with open('iris.data', newline='') as csvdosyasi:
    okuyucu = csv.DictReader(csvdosyasi)

    for satir in okuyucu:
        print(satir)
        print(satir["species"])