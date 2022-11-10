pesos = { "Cisco":[68,78,87], "Joel":[89,92,94]};
pesos["Pepe"]=[56,59,62];

try:
    nom = input("nom → ");
    pes = int(input("pes → "));
    pesos[nom].append(pes);
    n = 3
    while n>0:
        a = []
        s = 0
        pes1 = pesos[nom][s]
        pes2 = pesos[nom][s+1]
        dif = pes2 - pes1
        a.append(dif)
        s += 1
        n = n-1
        print("Pesos de", nom, "→",pesos[nom], a);
        
    print("Pesos de", nom, "→",pesos[nom], a) 
    
    
except:
    pesos[nom]=[pes];

    print("Pesos de", nom, "→",pesos[nom]);



    