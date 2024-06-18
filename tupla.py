tupla=(1,2,3)
type(tupla)
a,b,c=tupla
print(a)
print(b)
print(c)
for i in tupla:
    print(i)

if 3 in tupla:
    print("el numero 3 esta en la tupla")

tupla2=(4,5,6)
tupla3=tupla+tupla2
print(tupla3)