

#Übung 1

###
eingabe = int(input("was sit di Drehzahl"))
if eingabe >= 3000 :
    print("zu hohe drehzahl")

###


#Übung2

###
druck = float(input("was ist der Druck"))

ausgabe = f"falscher input"

if druck < 50 :
    ausgabe = f"fehler. Druck zu niedrig ({druck} bar)"
else:
    ausgabe = f"Druck OK ({druck} bar)"

print(ausgabe)
###


#Übung 3

###
kraft = int(input("Kraft: "))
quer = int(input("querschnitt: "))
sigma = kraft / quer

if sigma < 100:
    klasse = f"Niedrigspannung"

elif sigma < 235:
    klasse = f"Betriebspannung"

elif sigma < 360:
    klasse = f"Grenzspannung"

elif sigma >= 360:
    klasse = f"Bruchspannung"

print(f"Spannung: {sigma} MPa")
print(f"Klasse: {klasse}")
###

#Übung 4

###
material = [aluminium, Stahl, Edelstahl]
komplexität = [Einfach, Mittel, Schwer]

barbeitung = input("berb. Zeit: ")
material = input("")
print(material)