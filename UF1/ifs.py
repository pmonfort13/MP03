num = 36
candidat=int(input("numero 0 - 100:"));

if (candidat>100 or candidat<0):
    print("\n he dit entre 0 i 100");
elif candidat > num:
    print("\n T'has passat!");
elif candidat == num :
    print("\n Has encertat!");
else: 
    print("\n T'has quedat curt!");