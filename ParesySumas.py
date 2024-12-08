#Número de pares en una lista cuya suma sea igual a un objetivo:
#Entrada: arr = [1, 2, 3, 4, 3, 2, 1], target = 4
#Salida: 3 (Los pares son: (1, 3), (2, 2), (3, 1)

arr = [1, 2, 3, 4, 3, 2, 1]
target = 4
seen={}

for x in range (0,len(arr)-1):
    num1=arr[x]
    for n in range(0,len(arr)-1):
        num2=arr[n]
        if ((num1+num2)==target):
            
            if(not num1 in seen):            
                seen[num1] =1
                print(f"({num1},{num2})")    
            
