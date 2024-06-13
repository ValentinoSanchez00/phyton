import math
""" Ejercicio 1 """
""" for i in range(1,11):
    print("Tabla del %i" % i)
    for j in range(1,11):
     print("%i x %i = %i" % (i, j, j*i)) """

""" Ejercicio 2 """
""" año=2001
while año <= 2024:
    print("Informe del año ", año)
    año+=1 """

""" Ejercicio 3 """
""" for i in range(10):
    print(i) """

""" Ejercicio 4 """
""" for caracter in "hola":
    print(caracter) """

""" Ejercicio 5 """
""" for i,j in zip(range(1,4),["ana","juan","pepe"]):
    print(i,j)
 """

""" Ejercicio 6 """
""" num= int(input("ingrese un numero \n"))
print("Tabla del %i" % num)
for j in range(1,11):
     print("%i x %i = %i" % (num, j, j*num)) """
     
"""Otra Opcion"""
""" num= int(input("ingrese un numero \n"))
print("Tabla del %i" % num)
i=0
while i<=10:
    print("%i x %i = %i" % (num, i, num*i))
    i+=1 """
    
""" Ejercicio 7 """
import random
import os
intentos=0
num_aleatorio = random.randint(1,100)
os.system("cls")
numUser=int(input("ingrese un numero \n"))
while numUser!=num_aleatorio:
    if numUser>num_aleatorio:
        os.system("cls")
        print("el numero es menor")
        intentos+=1
    else:
        os.system("cls")
        print("el numero es mayor")
        intentos+=1
    numUser=int(input("ingrese un numero \n"))
print("acertaste, numero de intentos %i" % intentos)