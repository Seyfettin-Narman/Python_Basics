dicti={
    "maaş":7500,
    "mevki": "Ar-Ge",
    "görev süresi(yıl)": 10
}
print(dicti)
print(dicti["maaş"])
print(dicti["mevki"])
print(dicti["görev süresi(yıl)"])
dicti["adısoyadı"] = "Seyfettin Narman"
print(dicti)
print(dicti["adısoyadı"])
dicti["adısoyadı"]="Murat Narman"
print(dicti)
print(dicti.keys())
print(dicti.values())
for i in dicti.keys():
    print(i,":",dicti[i])