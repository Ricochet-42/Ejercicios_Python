#ordenamiento burbuja
flagi=False
arreglo=[7,4,9,12,43,5,10,2,1,29,3,1]
while not flagi:
    count=0
    for x in range(0,len(arreglo)-1):
        if (arreglo[x]>arreglo[x+1]):
            aux=arreglo[x+1]
            arreglo[x+1]=arreglo[x]
            arreglo[x]=aux
            count=count+1
    if(count==0):
        flagi=True
    print (arreglo)
    
    
