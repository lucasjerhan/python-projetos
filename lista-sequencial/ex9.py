altura = float(input("Digite a altura da pessoa (em metros): "))
genero = input("Digite o gênero da pessoa (M para masculino, F para feminino): ")

if genero.upper() == "M":
    peso_ideal = (72.7 * altura) - 58
    print(f"O peso ideal para um homem com essa altura é: {peso_ideal:.2f} kg")
elif genero.upper() == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"O peso ideal para uma mulher com essa altura é: {peso_ideal:.2f} kg")
else:
    print("Gênero inválido. Por favor, digite M para masculino ou F para feminino.")