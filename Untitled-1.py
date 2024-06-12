""" Ej 1 """
""" nombre=input("ingrese su nombre \n")
print("hola " + nombre) """

""" Ej 2 """
""" base=float(input("ingrese la base del triángulo \n"))
altura=float(input("ingrese la altura del triángulo \n"))
area=base*altura/2
perimetro=base*2+altura*2 """
""" %.2f = 2 decimales """
""" print("Resultado: Area=%.2f Perimetro=%.2f " % (area, perimetro)) """

""" Ej 3 """
""" import math
radio = float(input("ingrese el radio del circulo \n"))
area=  math.pi*radio**2
perimetro=2*math.pi*radio """
""" %.2f = 2 decimales """
""" print("Resultado: Area=%.2f Perimetro=%.2f " % (area, perimetro)) """

""" Ej 4 """
""" num1= float(input("ingrese el primer numero \n"))
num2= float(input("ingrese el segundo numero \n"))
suma=num1+num2
resta=num1-num2
multiplicacion=num1*num2
division=num1/num2 """
""" %.2f = 2 decimales """
""" print("la suma es %f \n la resta es %f \n la multiplicacion es %f \n la division es %.2f \n" % (suma, resta, multiplicacion, division)) """

""" Ej 5 """
palabra=input("ingrese una palabra \n")
""" Primera Opción """
""" for i in range(1000):
    print(palabra, sep="  \n") """

""" Segunda Opción """
print((palabra + " ")*1000)