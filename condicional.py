a = False

print(type(a))
if a :
    print("Verdadeiro")
else:
    print("Falso")

    #a>b a<b a>=b a<=b
    # a!=b diferente
    # a == b igual com dois sinais de igual senao atribui valor

    n1 = 50
    n2 = 12

    #n1 é maior do que n2

    """
    if n1>n2:
        print("n1 é maior do que n2")
    else:
        print("n1 é menor do que n2")
    nome = input("Digite um nome : ")

    if nome == "jose":
        print("É igual")
    else:
        print("É diferente")
      """ 


    nome = input("Digite seu nome")
    nota1 = float(input("Digite sua nota1"))
    nota2 = float(input("Digite sua nota2"))
    nota3 = float(input("Digite sua nota3"))
    media = (nota1 + nota2 + nota3) / 3
    
    
    print("Sua media é ", media)
    if media >= 7:
        print ("O aluno", nome,"esta aprovado")
    elif media<5:
        print ("O aluno", nome,"esta reprovado")
    else:
        print("O aluno", nome,"esta Apavorado")        
       