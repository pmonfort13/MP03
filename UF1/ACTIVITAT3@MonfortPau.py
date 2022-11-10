#GAUDIM DE LES LLISTES:

#Realitza els següents programes i lliura el codi font, RECORDA que aquest cop has d'operar amb llistes:

#Crea un programa que demani una cadena de 4 caràcters (numèrics) a l'usuari, (com "1234") els emmagatzemi a una llista convertits en enters i imprimeixi la suma dels números que la formen. Heu d'utilitzar una funció interna per a fer la suma.

cadena = input("Digues una cadena de 4 nombres: ");

try:

 llista = [int(cadena[0]), int(cadena[1]), int(cadena[2]), int(cadena[3])];

except:
 print("No has intrduit nombres!!")

else:
 print("\n la suma dels nombres és: " + str((sum(llista))));

#Demana a l'usuari un número i afegeix-lo al final de la llista amb un mètode de llista.

num = int(input("\n Digues un altre nombre"));
llista.append(num); 
print("No has intrduit nombres!!")
print("\n La llista amb el nombre és: " + str(llista));


#Ara elimina aquest número de la llista amb un mètode de llista.
llista.pop();
print("\n La llista sense l'ultim afegit és: " + str(llista));


#Ordena la llista amb un mètode de llista.

llista.sort();
print("\n La llista ordenada és: " + str(llista));


#Mostra el seu número màxim i el seu mínim, extrets amb funcions internes.

print("\n El màxim és: " + str(max(llista)));
print("\n El  minim és: " + str(min(llista)));


#Calcula la mitjana aritmètica de la llista a partir de les funcions internes sum() i len().

suma = sum(llista);
digits = len(llista);
mitjana = int(suma) / int(digits);
print("\n La mitjana dels nombres és: " + str(mitjana));