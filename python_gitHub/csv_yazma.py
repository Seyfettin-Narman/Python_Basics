import csv

baslik1 = ["sicaklik", "nem", "basinc"]

veriler = [[30, 75.5, 10], [32.3, 50, 3]]

with open('sensorverileri.csv','w', encoding='UTF8', newline='') as file:

    writer = csv.writer(file)
    writer.writerow(baslik1)
    writer.writerows(veriler)