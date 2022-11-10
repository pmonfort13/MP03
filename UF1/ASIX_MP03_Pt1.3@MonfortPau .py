#Tasca1:
#Escriu un programa que sol·liciti una puntuació entre 0 i 10. Si la puntuació és fora d'aquest rang, mostra un missatge d'error. Si la puntuació està entre 0 i 10, mostra la qualificació usant la taula següent:
#Puntuació Qualificació
#>= 9 Excel·lent
#>= 8 Notable
#>= 7 Bé
#>= 5 Suficient
#< 5 Insuficient
#Bateria de proves:
#Introduïu puntuació: 9.5 -> Excel·lent
#Introduïu puntuació: perfecte -> Puntuació incorrecta
#Introduïu puntuació: 11 Puntuació -> Incorrecta
#Introduïu puntuació: 7.5 -> Bé
#Introduïu puntuació: 0.5 -> Insuficient
menu= int(input('''
MENU:
[1] NOTA
[2] ANYS
[3] JOC DAUS
        '''))

if menu == 1:

    n = False

    while n == False:
        try:
            nota = float(input("nota → \n"))


            if nota > 10 or nota < 0:
                print("La nota introduida és incorrecta")

            elif nota >= 9:
                print("Excel·lent")
                n=True
            elif nota >= 8:
                print("Notable")
                n=True
            elif nota >= 7:
                print("Bé")
                n=True
            elif nota >= 5:
                print("Suficient")
                n=True
            elif nota < 5:
                print("Insuficient")
                n=True

        except:
            print("Puntuació incorrecta")  




    #Tasca 2:
    #Escriu un programa que demani l'any actual i un altre any qualsevol. El resultat ha de mostrar quants anys han passat des de l'any introduït o quants anys falten.
    #Ara milloreu el programa per a fer que quan la diferència sigui només d'un any, ens digui que només falta un any.
elif menu == 2:    
    n = False

    while n == False:

        try:
            any1 = int(input("Digues l'any actual \n"))
            any2 = int(input("Digues un altre any \n"))

            if any1 == any2:
                print("Són el mateix any")
                n=True

            else:
                if any1 > any2:
                    difer=any1-any2
                    print("Han passat ", difer, " anys")
                    n=True
                elif any1 < any2:
                    difer=any2-any1
                    if difer == 1:
                        print("Nomes falta un any")
                        n=True
                    else:
                        print("Falten ", difer, " anys")
                        n=True


        except:
            print("No has introduit un any")





    #Tasca 3:
    #Creeu un joc de daus on es generi una tirada per a cadascun dels jugadors, quan escriguin la paraula "tirar" en un input i posteriorment es mostri el resultat de la partida.
    #Podeu utilitzar la funció randint() de la llibreria random:
    #Exemple d'ús:
    #numero = random.randint(1, 6)

elif menu == 3:
    import random
    n = False
    contador = 1

    while n == False:
        contador+1

        try:

            print("\n<<<< PARTIDA", contador,">>>>")
            tirar1=input("JUGADOR 1 → ESCRIU 'tirar' PER JUGAR\n")

            if tirar1 == "tirar":
                jug1= random.randint(1,6)
                print("JUGADOR 1 → ", jug1, "\n")
                tirar2=input("JUGADOR 2 → ESCRIU 'tirar' PER JUGAR\n")

                if tirar2 == "tirar":
                    jug2= random.randint(1,6)
                    print("JUGADOR 2 → ", jug2, "\n")
                    if jug1 == jug2:
                        print(jug1, " = ", jug2)
                        print("\nEMPAT")
                        contador += 1

                        cont=input("\n\nESCRIU 'EXIT' PER ACABAR DE JUGAR: ")
                        if cont.upper == "EXIT":
                            n = True

                    elif jug1 > jug2:
                        print(jug1, " > ", jug2)
                        print("\nEL JUGADOR 1 GUANYA!")
                        contador += 1


                        cont=input("\n\nESCRIU 'EXIT' PER ACABAR DE JUGAR: ")
                        if cont.upper == "EXIT":
                            n = True

                    elif jug1 < jug2:
                        print(jug1, " < ", jug2)
                        print("\nEL JUGADOR 2 GUANYA!")
                        contador += 1

                        cont=input("\n\nESCRIU 'EXIT' PER ACABAR DE JUGAR: ")
                        if cont.upper == "EXIT":
                            n = True

                else:
                    print("NO HAS ESCRIT LA PARAULA CORRECTA")

            else:
                print("NO HAS ESCRIT LA PARAULA CORRECTA")


        except:
            print("No has introduit el valor correcte")

