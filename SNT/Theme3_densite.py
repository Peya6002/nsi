#Lire fichier CSV
f = open("Theme3_Population.csv", "r")
print ("Formule de la densité = habitants/superficie")
print("")
entete = f.readline()
popEurope = 0
supEurope = 0
ligne = f.readline()
while ligne != "":
    nom,pop,sup = ligne.split(";")
    densitéPays = int(pop)/float(sup)
    ligne = f.readline()
    print("Pays: ", nom, "Densité: ", densitéPays," hab/km²")

f.close()