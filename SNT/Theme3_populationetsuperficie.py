#Neel Grevy 2nde2
f = open("Theme3_Population.csv", "r")
entete = f.readline()
popEurope = 0
supEurope = 0
ligne = f.readline()
while ligne != "":
    nom,pop,sup = ligne.split(";")
    popEurope = popEurope + int(pop)
    supEurope = supEurope + float(sup)
    ligne = f.readline()
print("Population totale : ", popEurope, "habitants")
print("Population totale : ", supEurope,"km²")
f.close()