import random

pregunta = [["Quin és el meu nom? : Joan : Pau : Pere",2],["Quina edat tinc? : 1 : 21 : 18",3]]


num = random.randint(0,1)

split = pregunta[num][0].split(":")
res = 0
print("_____PREGUNTA 1_____\n", split[0],"\n a)", split[1], "\n b)", split[2], "\n c)", split[3])

resposta = input()
if resposta == "a":
    res = 1 
elif resposta == "b":
    res = 2
elif resposta == "c":
    res = 3
else:
    print("Resposta no valida")

if res == pregunta[num][1]:
    print("RESPOSTA CORRECTA!")
else:
    print("RESPOSTA INCORRECTA")