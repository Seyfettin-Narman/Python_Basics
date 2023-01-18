import pandas as pd

veriler = pd.read_csv("iris.data")

print(veriler.head())
print(veriler.columns)
print(veriler[2:5])

veriler = veriler.sort_values(by="sepal_length")
print(veriler.head())

toplamVeri = veriler["sepal_length"].sum()
medyanVeri= veriler["sepal_length"].median()
ortalamaVeri = veriler["sepal_length"].mean()


print("Toplam:", toplamVeri, "\nOrtalama:", ortalamaVeri, "\nortanca:", medyanVeri)