lista=[1,2,3,4,5]
for i in lista:
    print(i)
    
if 3 in lista:
    print("el numero 3 esta en la lista")

lista+=[6,7,8,9,10]
print(lista)
sortedlista=sorted(lista)
sortedlista.reverse()
print(sortedlista)