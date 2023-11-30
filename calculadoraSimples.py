#pegar dois numeros e efetuar mostrando na tela 
# a soma, divisão, multiplicação e subtração da seguinte maneira
#exemplo:
#a soma dos dois numeros é : SOMA

n1 = int (input("Digite seu primeiro numero :"))
n2 = int (input("Digite seu segundo numero :"))

soma = n1 + n2 
subtracao = n1 - n2
divisao = n1 / n2
multiplicacao = n1* n2


print("A soma dos numeros é  : ",n1+n2)            
print("A subtracao dos numeros é  : ",subtracao)            
print("A divisao dos numeros é  : ",divisao)          
print(type(divisao))          
print("A multiplicacao dos numeros é  : ",multiplicacao)            