#palindromo
#reconocer
palabra=input("ingrese la palabra")
count=0

for x in range (0,len(palabra)):#no toca el ultimo valor
    
    if(palabra[x]==palabra[-x-1]):#si la primer letra 0 igual que la -1
        count+=1
    
if(count==len(palabra)):
    print("es palindromo")
else:
    print("no es palindromo")