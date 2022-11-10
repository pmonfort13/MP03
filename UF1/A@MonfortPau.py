print()
numif=int(input("QUE VOLS FER? \n MITJANA → 1 \n CALCUL IMC → 2 \n CANVI TEMPERATURA → 3 \n CALCUL TEMPS → 4"));

if numif == 1:
    #EXERCICI 1 - MITJANA
    num1=int(input("digues un numero: "));
    num2=int(input("digues un altre numero: "));

    mitj= (num1+num2)/2
    print("\nLa mitjana és "+ str(mitj))

elif numif==2:
    #EXERCICI 2 - IMC
    altura = float(input("\nQuina és la teva altura en m ? "))
    pes = int(input("Quin és el teu pes en kg ? "))

    estatura = altura ** 2
    imc = pes // estatura
    print("\nEl teu IMC és de "+ str(imc))
elif numif==3:
    #EXERCICI 3 - TEMPERATURA
    tempC = float(input("\nDigues una temperatura en Celsius: "))
    tempF = (tempC *1.8)+ 32
    print("\nLa teva temperatura en Fahrenheit és: "+ str(tempF))

elif numif==4:
    #EXERCICI 4 - TEMPS
    hora=int(input("\nDisme una hora: "))
    minuts=int(input("Disme els minuts: "))

    min1=hora*60
    min_total= min1 + minuts
    segons= min_total*60
    print("\nL'hora i minuts que has dit en segons és: "+str(segons))

else:
    print("has posat un nombre fora del rang")