#true love

frase="TRUELOVE"
count=0

n1=(input("Ingrese el primer nombre"))
n2=(input("Ingrese el segundo nombre"))
n1=n1.upper()
n2=n2.upper()
for x in range(0, len(n1)):
    if(n1[x] in frase):
        count+=1
    
for x in range(0, len(n2)):
    if(n2[x] in frase):
        count+=1
        
print(f"el resultado es {count}")