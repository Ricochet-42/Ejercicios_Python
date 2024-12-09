#supongamos que estamos en un concurso
#hay una lista de participantes
#quiero que la computadora de manera aleatoria
#seleccione a la siguiente persona en irse
#VIc Broda

import random

lista=["kiara","doris","sheila","emiliano","chuy","chris"]



def salir():
    fuera=random.choice(lista)
    print(f"{fuera} queda fuera")
    lista.remove(fuera)  
    print(f"Participantes restantes: {lista}")
    
    



flag=False
while (flag == False):
    
    if(len(lista)==1):
        print(f"El ganador es {lista}")
        break
        
    res=int(input("desea continuar? 1=si"))
    if(res==1):
        salir()
    else:
        print(lista)
        flag=True



