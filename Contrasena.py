#hagamos un programa que sea un generador de contraseñas
#este programa debe pedir al usuario
#la cantidad de letras de la contraseña
#la cantidad de numeros
#la cantidad de simbolos a utilizar
#tiene que generar una contraseña en ese orden en función de lo dado por el usuario
import random
letras="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
numeros="1234567890"
signos="!@#$%^&*()_+-=}{[]\|:';?/>.<,"

contra=[]
l=int(input("cuantas letras requiere"))
n=int(input("cuantos numeros requiere"))
c=int(input("cuantos caracteres requiere"))

for x in range(0,l):#el cero cuenta
    contra.append(random.choice(letras))
    

for x in range(0,n):
    contra.append(random.choice(numeros))
    

for x in range(0,c):
    contra.append(random.choice(signos))

#print (contra)
random.shuffle(contra)
print (contra)