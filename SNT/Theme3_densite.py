#Lire fichier CSV
f = open("Theme3_Population.csv", "r")

print("")
entete = f.readline()
popEurope = 0
supEurope = 0
ligne = f.readline()
while ligne != "":
    nom,pop,sup = ligne.split(";")
    densitéPays = int(pop)/float(sup)
    ligne = f.readline()
    print("Pays: ", nom, "Densité: ", densitéPays)

f.close()
