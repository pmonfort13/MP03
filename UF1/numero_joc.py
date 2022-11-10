n = 5
import random
res = random.randint(1,100)

while n>0:
    num = int(input("\n num entre 1 - 100"))

    if num > 100 or num < 1:
        print("\n error")
        
    elif num == res:
        print("\n ENCERT!!")
        break

    else:
        print("\n INCORRECTE, et queden", n-1, "intents")
        n = n-1
