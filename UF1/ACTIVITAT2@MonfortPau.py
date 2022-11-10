#AC1
#Crea un programa que a partir d'una cadena de 4 caràcters (numèrics) preguntada a l'usuari, (com "123456") imprimeixi la suma dels números que la formen. 
#Teniu en compte que només s'ha d'utilitzar un input, estem treballant les cadenes.

cadena1 = input("Digues una cadena de 4 caracters nombres: ");

num1 = int(cadena1[0]);
num2 = int(cadena1[1]);
num3 = int(cadena1[2]);
num4 = int(cadena1[3]);

suma = num1+num2+num3+num4;

print("\n La suma dels 4 nombres és " + str(suma));


#AC2
#Consulta els mètodes "built-in" que teniu disponibles per a cadenes i crea un programa que a partir d'una frase donada per l'usuari calculi:

frase = input("\n Digues una frase: ");

#Número de caràcters.
ncaracters = len(frase);
print ("\nNúmero de caràcters: " + str(ncaracters));

#Número de paraules.
paraules = frase.split( );
nparaules = len(paraules);
print ("\nNúmero de paraules: " + str(nparaules));

#Frase  amb totes les paraules en majúscula.
mayus = frase.upper();
print (mayus);

#Frase  amb totes les paraules en minúscula.
minus = frase.lower();
print (minus);



caracter = input("\nDigues un caràcter: ");

#Preguntat un caràcter a l'usuari retorni la posició de la primera coincidència trobada a la frase.
poscaracter1 = minus.find(caracter)+ 1;
print("\nEl primer caracter que coincideix és el: "+ str(poscaracter1));

#Preguntat un caràcter a l'usuari retorni la posició de la darrera coincidència trobada a la frase.
poscaracter2 = minus.rfind(caracter)+ 1;
print("\nL'ultim caracter que coincideix és el: "+ str(poscaracter2));

#Preguntat un caràcter a l'usuari retorni el número de coincidències trobades a la frase.
ncoincidencia = minus.count(caracter);
print("\nEl caracter ("+ str(caracter)+ ") apareix "+ str(ncoincidencia) + " vegades.");

#Mostri el número de vocals del text (has d'optimitzar al màxim aquest codi!!).
nvocals = minus.count("a") + minus.count("e") + minus.count("i") + minus.count("o") + minus.count("u");
print ("\nNombre de vocals: "+ str(nvocals));



#Modifica el primer programa per a que abans de donar el resultat mostri si és cert que la cadena només conté números.
cadena1 = input("\nDigues una cadena de 4 caracters nombres: ");

print ("\nLa cadena només conté numeros = "+ str(cadena1.isnumeric()));