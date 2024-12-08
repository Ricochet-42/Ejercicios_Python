#busqueda numerica

rango=1000
flag=False
inicio=0
while flag==False:
    mitad=inicio+(round((rango-inicio)/2))
    res=int(input(f"{mitad} 1-mayor 2-menor 3-igual"))

    if (res==1):
        inicio=mitad
       
    elif (res==2):
        rango=mitad    
        
    else:
        print(f"tu numero es {mitad}")
        flag=True
        
