# Labo 01 - basisvariabelen

dag = int(input("Geef de dagen op \n"))
uur = int(input("Geef de uren op \n"))
minuut = int(input("Geef de minuten op \n"))
seconden = int(input("Geef de seconden op \n"))

dag = int(dag*86400)
uur = int(uur*3600)
minuut = int(minuut*60)
seconden = int(seconden)

tijd = int(dag + uur + minuut + seconden)
tijd = str(tijd)
print("Het aantal seconden zijn: ",tijd,"")

