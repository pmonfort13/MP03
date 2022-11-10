import random
a = False
max=9
res = 0
#####PREGUNTES#####
pregunta = [
    ["¿Cada cuántos años se celebran los Juegos Olímpicos?",[["2",False],["4",True],["6",False]]],
    ["¿En qué ciudad española está el estadio de fútbol de Mestalla?", [["Barcelona",False],["Cadiz",False],["Valencia",True]]],
    ["¿En qué año el hombre pisó la Luna por primera vez?",[["1979",False],["1969",True],["1967",False]]],
    ["¿Quién fue el primer presidente de Estados Unidos?", [["George Washington", True], ["James Buchanan",False], ["Donald Trump",False]]],
    ["¿Cuánto duró la Guerra de los Cien Años?", [["98 años", False], ["116 años",True], ["100 años",False]]],
    ["¿En qué año se creó la Organización de las Naciones Unidas?",[["1945",True],["1937",False],["1963",False]]],
    ["¿Qué carabela no volvió del viaje en el que Colón arribó a América por primera vez?", [["La Pinta",False],["La Niña",False],["La Santa Maria",True]]],
    ["¿Cuál es la lengua más hablada del mundo?",[["Ingles",False],["Chino Mandarin",True],["Ruso",False]]],
    ["¿En qué otro idioma, además del castellano, escribió la novelista y poetisa Rosalía de Castro?", [["Catalan",False],["Euskera",False],["Gallego",True]]],
    ["¿Cuándo se celebró la primera Copa Mundial de Fútbol?",[["1930",True],["1936",False],["1940",False]]],
    ]
###################
#####CONTADORS#####
npreg = 1
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
###################
input('''
_________TRIVIAL PURSUIT_________
PULSA ENTER PER COMENÇAR A JUGAR
_________________________________
''')
#######JUGADORS#######
jugadors = []
i = int(input("\nSELECCIONA EL NOMBRE DE JUGADORS 2 - 4: "))
jmax = i
j = 1
while i > 0 :
    jugadors.append(input("\n Jugador "+str(j)+" - introdueix el teu nom:"))
    i -= 1
    j += 1
jug = random.randint(1,jmax)
indx = jug-1
print("\nEL JUGADOR", jug, "COMENÇA: \n")
print(jugadors[indx],"ES EL TEU TORN:")
######################
while a==False:
    nump = random.randint(0,max)
    numr = [0,1,2]
    random.shuffle(numr)

    print("\n_____ PREGUNTA",npreg,"_____\n", pregunta[nump][0],"\n a)", pregunta[nump][1][numr[0]][0], "\n b)", pregunta[nump][1][numr[1]][0], "\n c)", pregunta[nump][1][numr[2]][0])
    max -= 1

    resposta = input().lower()
    if resposta == "a":
        res = pregunta[nump][1][numr[0]][1] 
    elif resposta == "b":
        res = pregunta[nump][1][numr[1]][1]
    elif resposta == "c":
        res = pregunta[nump][1][numr[2]][1]
    else:
        print("RESPESTA NO CORRECTA")
        res = False
    if max == 0:
        a = True
    elif res == True:
        del pregunta[nump]
        print("RESPOSTA CORRECTA!")
        npreg = npreg+1
        if jug == 1:
            cont1 = cont1 + 1
            print("\n JUGADOR", jug,"PORTES", cont1,"RESPOSTES CORRECTES")
            input("\nPULSA ENTER PER CONTINUAR") 
            if cont1 ==3 or cont2 ==3 or cont3 ==3 or cont4 ==3:
                a = True
            else:
                a = False
        elif jug ==2:
            cont2 = cont2 + 1
            print("\n JUGADOR", jug,"PORTES", cont2,"RESPOSTES CORRECTES")
            input("\nPULSA ENTER PER CONTINUAR")
            if cont1 ==3 or cont2 ==3 or cont3 ==3 or cont4 ==3:
                a = True
            else:
                a = False
        elif jug ==3:
            cont3 = cont3 + 1
            print("\n JUGADOR", jug,"PORTES", cont3,"RESPOSTES CORRECTES")
            input("\nPULSA ENTER PER CONTINUAR")
            if cont1 ==3 or cont2 ==3 or cont3 ==3 or cont4 ==3:
                a = True
            else:
                a = False
        elif jug ==4:
            cont4 = cont4 + 1
            print("\n JUGADOR", jug,"PORTES", cont4,"RESPOSTES CORRECTES")
            input("\nPULSA ENTER PER CONTINUAR")
            if cont1 ==3 or cont2 ==3 or cont3 ==3 or cont4 ==3:
                a = True
            else:
                a = False
    else:
        print("RESPOSTA INCORRECTA")
        npreg = npreg+1
        del pregunta[nump]
        indx += 1
        jug += 1
        if indx + 1 > jmax:
            indx = 0
            jug = 1
            print("\n JUGADOR", jug,"ÉS EL TEU TORN:\n")
            input("\nPULSA ENTER PER CONTINUAR")
        else:
            print("\n JUGADOR", jug,"ÉS EL TEU TORN:\n")
            input("\nPULSA ENTER PER CONTINUAR")
if max == 0:
    print("\nS'HAN ACABAT LES PREGUNTES, NO GUANYA NINGU :(")
elif cont1 == 3: 
    print("\nFELICITATS", jugadors[0],"ETS EL GUANYADOR!!")
elif cont2 == 3:
    print("\nFELICITATS", jugadors[1],"ETS EL GUANYADOR!!")
elif cont3 == 3:
    print("\nFELICITATS", jugadors[2],"ETS EL GUANYADOR!!")
elif cont3 == 3:
    print("\nFELICITATS", jugadors[3],"ETS EL GUANYADOR!!")