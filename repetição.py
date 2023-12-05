#Comandos de repetição

for x in range (5,11):
    print(x)
listNomes = ["Maria","Ana","Pedro","João"]

for x in listNomes:
    print(x)
numeros = (3,6,4,9)
soma = 0 
for x in numeros:
    soma += x
print(soma) #mostra a soma toda vez que passa pelo for
print("O resultado todal é : ",soma)

i = 0
while i<10:
      print(i)
      i+=1

lista = ["fanta","coca","sprite","tai","skol","bohemia"] 
i = 0

while i < len(lista):
     #print (i," - ", lista[i])
     print(i," - ", lista[i])
     i+=1

