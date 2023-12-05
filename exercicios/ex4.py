nome = str(input("Digite o nome do vendedor"))
salariofixo = float(input("Digite o salario fixo do vendedor"))
totalvendas = float(input("Digite o total de vendas"))

comissao = totalvendas * 0.15 + salariofixo

print("Nome:",nome)
print("Salario fixo:",salariofixo)
print("Salario final", comissao)