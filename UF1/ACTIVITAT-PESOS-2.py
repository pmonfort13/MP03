pesos = { "Cisco":[68,78,87], "Joel":[89,92,94]};
pesos["Pepe"]=[56,59,62];

try:
    nom = input("nom → ");
    pes = int(input("pes → "));
    pesos[nom].append(pes);

    print("Pesos de", nom, "→",pesos[nom]); 
    
    
except:
    pesos[nom]=[pes];

    print("Pesos de", nom, "→",pesos[nom]);



    
