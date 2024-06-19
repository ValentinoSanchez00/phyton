""" Modos de acceso
Los modos que podemos indicar son los siguientes:

Añadido en modo binario. Crea si éste no existe
Modo	Comportamiento	Puntero
r	Solo lectura	Al inicio del archivo
rb	Solo lectura en modo binario	
r+	Lectura y escritura	Al inicio del archivo
rb+	Lectura y escritura binario	Al inicio del archivo
w	Solo escritura. Sobreescribe si existe. Crea el archivo si no existe.	Al inicio del archivo
wb	Solo escritura en modo binario. Sobreescribe si existe. Crea el archivo si no existe.	Al inicio del archivo
w+	Escritura y lectura. Sobreescribe si existe. Crea el archivo si no existe.	Al inicio del archivo
wb+	Escritura y lectura binaria. Sobreescribe si existe. Crea el archivo si no existe.	Al inicio del archivo
a	Añadido (agregar contenido). Crea el archivo si no existe.	Si el archivo existe, al final de éste. Si el archivo no existe, al comienzo.
ab		Si el archivo existe, al final de éste. Si el archivo no existe, al comienzo.
a+	Añadido y lectura. Crea el archivo si no existe.	Si el archivo existe, al final de éste. Si el archivo no existe, al comienzo.
ab+	Añadido y lectura en binario. Crea el archivo si no existe	Si el archivo existe, al final de éste. Si el archivo no existe, al comienzo.
 """
 
""" f=open("ejemplo1.txt","w")
f.write(input("Introduce un texto: "))
f.close() """

with open("ejemplo1.txt","r") as archivo:
    """ contenido=archivo.read
    print(contenido) """
    """ for linea in archivo:
        print(linea) """

""" leer fichero csv """
import csv
""" 
fichero=open("Ejemplocsv.csv","r")
contenido=csv.reader(fichero,delimiter=";")
for linea in contenido:
    print("fila "+str(contenido.line_num)+" "+str(linea)) """
    
""" 
fichero=open("Ejemplo2csv.csv","w")
contenido=csv.writer(fichero,delimiter=";")
contenido.writerow(["nombre","edad", "genero"])  
for i in range(5):
    nombre=input("ingrese un nombre \n")
    edad=int(input("ingrese una edad \n"))
    genero=input("ingrese un genero \n")
    contenido.writerow([nombre,edad,genero])  """
      
import json

# Lee el archivo JSON
with open("ejemplojson.json", "r") as file:
    datos = json.load(file)

# Agrega el nuevo alumno
alumno={
    "nombre": input("ingrese un nombre \n"),
    "apellidos": input("ingrese un apellido \n"),
    "direccion": {
        "calle": input("ingrese una calle \n"),
        "numero": int(input("ingrese un numero \n"))
    },
    "notas": []
}
for i in range(5):
    alumno["notas"].append(int(input("ingrese una nota \n")))

datos["clase"]["alumno"].append(alumno)

    

# Escribe los datos actualizados de nuevo en el archivo JSON
with open("ejemplojson.json", "w") as file:
    json.dump(datos, file, indent=4)  # indent=4 es para hacer el archivo más legible


