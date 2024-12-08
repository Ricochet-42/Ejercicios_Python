def triPascal(n):
    arr=[]
    
    if (n == 1):
        arr.append(1)#agregar 1
        print(arr)
        
    else:
        aux = triPascal(n-1)#arreglo anterior
        arr.append(1)#uno inicial
        
        for x in range (0,len(aux)-1):#pasar por todos los valores del arreglo anterior
            arr.append(aux[x]+aux[x+1])#sumar los valores del arreglo anterior
            
            
        arr.append(1)#uno final
        print (arr)
        
    return arr
        
        
        
arreglo = triPascal(5)#numero de filas