import os
lista=[]
""" while num>0:
    os.system("cls")
    num=int(input("ingrese un numero \n") )
    lista.append(num)
else:
    os.system("cls")
    print("Numero maximo alcanzado")
    print(max(lista))
    print("Numero minimo alcanzado")
    print(min(lista))
    print("Numeros pares")
    for i in lista:
        if i%2==0:
            print(i, end=" ") """
            
def cuadrado(x):
    return x**2

def par(x):
    return x%2==0

lista=[1,2,3,4,5]
lista2=list(map(cuadrado, lista))
pares=list(filter(par, lista)) 

  
    