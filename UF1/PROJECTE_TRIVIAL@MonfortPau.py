import random
from os import system
import time
a = False
max=9
res = 0
g = False
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

      __^__                                      __^__
     ( ___ )------------------------------------( ___ )
      | / |                                      | \ |
      | / |           TRIVIAL PURSUIT            | \ |
      | / |                                      | \ |
      | / |   PULSA ENTER PER COMENÇAR A JUGAR   | \ |
      |___|                                      |___|
     (_____)------------------------------------(_____) 


''')
#TONTERIA TEXT QUE S'ESCRIU
jugadors = []
system("clear")

print("\n \n     H")
time.sleep(0.1)
system("clear")
print("\n \n     HO")
time.sleep(0.1)
system("clear")
print("\n \n     HOL")
time.sleep(0.1)
system("clear")
print("\n \n     HOLA")
time.sleep(0.1)
system("clear")
print("\n \n     HOLA J")
time.sleep(0.1)
system("clear")
print("\n \n     HOLA JU")
time.sleep(0.1)
system("clear")
print("\n \n     HOLA JUG")
time.sleep(0.1)
system("clear")
print("\n \n     HOLA JUGA")
time.sleep(0.1)
system("clear")
print("\n \n     HOLA JUGAD")
time.sleep(0.1)
system("clear")
print("\n \n     HOLA JUGADO")
time.sleep(0.1)
system("clear")
print("\n \n     HOLA JUGADOR")
time.sleep(1)
system("clear")

while g == False:
    i = int(input('''


                         (0 0) 
       -------------oOO-- (_) ----oOO------------    
      ╔══════════════════════════════════════════╗ 
      ║ SELECCIONA EL NOMBRE DE JUGADORS 2 - 4:  ║ 
      ╚══════════════════════════════════════════╝ 
       ------------------------------------------
                        |__|__| 
                         || || 
                        ooO Ooo 
    

    '''))

    if i > 4 or i < 1:
        print("\n||| HAS INTRODUIT UN NOMBRE INCORRECTE |||")
    else:
        g=True
system("clear")
jmax = i
j = 1
while i > 0 :
    print                   ("\n════════════════════════════════════════")
    jugadors.append(input("\n Jugador "+str(j)+" - introdueix el teu nom:"))

    i -= 1
    j += 1
print                   ("\n════════════════════════════════════════")  
jug = random.randint(1,jmax)
indx = jug-1
system("clear")
print('''


                         (0 0) 
       -------------oOO-- (_) ----oOO------------    
      ╔══════════════════════════════════════════╗ ''')
print("      ║          EL JUGADOR", jug, "COMENÇA:           ║")
print('''      ╚══════════════════════════════════════════╝ 
       ------------------------------------------
                        |__|__| 
                         || || 
                        ooO Ooo 
    

    ''')

######################
while a==False:
    system("clear")
    nump = random.randint(0,max)
    numr = [0,1,2]
    random.shuffle(numr)
    print("\n╔════════════════════════════════ PREGUNTA",npreg,"════════════════════════════════╗\n", pregunta[nump][0],"\n a)", pregunta[nump][1][numr[0]][0], "\n b)", pregunta[nump][1][numr[1]][0], "\n c)", pregunta[nump][1][numr[2]][0])
    max -= 1
    resposta = input().lower()
    if resposta == "a":
        res = pregunta[nump][1][numr[0]][1] 
    elif resposta == "b":
        res = pregunta[nump][1][numr[1]][1]
    elif resposta == "c":
        res = pregunta[nump][1][numr[2]][1]
    else:
        res = False
    if max == 0:
        a = True
    elif res == True:
        del pregunta[nump]
        system("clear")
        print('''
        ╔═.✵.═════════════════════╗
        ║    RESPOSTA CORRECTA    ║
        ╚═════════════════════.✵.═╝
        ''')
        time.sleep(1)
        npreg = npreg+1
        if jug == 1:
            cont1 = cont1 + 1
            system("clear")
            print("\n       JUGADOR", jug,"PORTES", cont1,"RESPOSTES CORRECTES")
            input('''


        ╔═════════════════════════════════╗
        ║    PULSA ENTER PER CONTINUAR    ║
        ╚═════════════════════════════════╝
        ''') 
            if cont1 ==3 or cont2 ==3 or cont3 ==3 or cont4 ==3:
                a = True
            else:
                a = False
        elif jug ==2:
            cont2 = cont2 + 1
            system("clear")
            print("\n       JUGADOR", jug,"PORTES", cont2,"RESPOSTES CORRECTES")
            input('''


        ╔═.✵.═════════════════════════════╗
        ║    PULSA ENTER PER CONTINUAR    ║
        ╚═════════════════════════════.✵.═╝
        ''')
            if cont1 ==3 or cont2 ==3 or cont3 ==3 or cont4 ==3:
                a = True
            else:
                a = False
        elif jug ==3:
            cont3 = cont3 + 1
            system("clear")
            print("\n       JUGADOR", jug,"PORTES", cont3,"RESPOSTES CORRECTES")
            input('''


        ╔═.✵.═════════════════════════════╗
        ║    PULSA ENTER PER CONTINUAR    ║
        ╚═════════════════════════════.✵.═╝
        ''')
            if cont1 ==3 or cont2 ==3 or cont3 ==3 or cont4 ==3:
                a = True
            else:
                a = False
        elif jug ==4:
            cont4 = cont4 + 1
            system("clear")
            print("\n       JUGADOR", jug,"PORTES", cont4,"RESPOSTES CORRECTES\n")
            input('''


        ╔═.✵.═════════════════════════════╗
        ║    PULSA ENTER PER CONTINUAR    ║
        ╚═════════════════════════════.✵.═╝
        ''')
            if cont1 ==3 or cont2 ==3 or cont3 ==3 or cont4 ==3:
                a = True
            else:
                a = False
    else:
        system("clear")
        print('''
        ╔═.✵.═══════════════════════╗
        ║    RESPOSTA INCORRECTA    ║
        ╚═══════════════════════.✵.═╝
        ''')
        time.sleep(1)
        npreg = npreg+1
        del pregunta[nump]
        indx += 1
        jug += 1
        if indx + 1 > jmax:
            indx = 0
            jug = 1
            system("clear")
            print("\n        JUGADOR", jug,"ÉS EL TEU TORN:\n")
            input('''


        ╔═════════════════════════════════╗
        ║    PULSA ENTER PER CONTINUAR    ║
        ╚═════════════════════════════════╝
        ''') 
        else:
            system("clear")
            print("\n        JUGADOR", jug,"ÉS EL TEU TORN:\n")
            input('''


        ╔═════════════════════════════════╗
        ║    PULSA ENTER PER CONTINUAR    ║
        ╚═════════════════════════════════╝
        ''') 
if max == 0:
    system("clear")
    print('''


        ╔══════════════════════════════════════════════════════╗
        ║    S'HAN ACABAT LES PREGUNTES, NO GUANYA NINGU :(    ║
        ╚══════════════════════════════════════════════════════╝
        ''')
else: 
    system("clear")
    print('''


        ╔══════════════════════════════════════════════════════╗''')
    print("        ║           FELICITATS", jugadors[indx],"ETS EL GUANYADOR!!          ║")
    print('''        ╚══════════════════════════════════════════════════════╝''')