valor_hora = float(input("Digite o valor que você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

salario = valor_hora * horas_trabalhadas

print(f"O total do seu salário no mês é: R${salario:.2f}")