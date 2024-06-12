""" Ejercicio 1 """
""" num1= float(input("ingrese el primer numero \n"))
num2= float(input("ingrese el segundo numero \n"))
suma=num1+num2
if suma > 0:
    print("la suma es positiva")
elif suma < 0:
    print("la suma es negativa")
else:
    print("la suma es 0") """

""" Ejercicio 2 """
""" num= float(input("ingrese un numero \n"))

if num%2 == 0:
    print("el numero es par")
else:
    print("el numero es impar") """

""" Ejercicio 3 """
""" mes= int(input("ingrese el mes \n"))
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    print("el mes tiene 31 dias")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("el mes tiene 30 dias")
elif mes == 2:
    print("el mes tiene 28 o 29 dias")
else:
    print("el mes no existe") """

""" Ejercicio 4 """
user="Valentino"
password="12345"

condicion= True
while condicion:
    compUser=input("ingrese su usuario \n")
    compPassword=input("ingrese su password \n")

    if user == compUser and password == compPassword:
        print("acceso autorizado")
        condicion=False
    else:
        print("acceso denegado \n\n")
