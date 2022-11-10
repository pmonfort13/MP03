dni = input("Digues el teu DNI: ");

try:
    nombre = int(dni[:-1]);
    lletra1 = dni[8:];
    lletra2 = lletra1.upper();

    residu = int(nombre) % 23;

    lletres = "TRWAGMYFPDXBNJZSQVHLCKE";
    lletracalcul = lletres[residu];

    print(lletra2 == lletracalcul);

except:
    print("T'has errat en algun lloc");