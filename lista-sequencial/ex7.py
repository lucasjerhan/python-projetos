numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero_real = float(input("Digite o número real: "))

resultado1 = (2 * numero1) * (numero2 / 2)
resultado2 = (3 * numero1) + numero_real
resultado3 = numero_real ** 3

print(f"O produto do dobro do primeiro com metade do segundo é: {resultado1}")
print(f"A soma do triplo do primeiro com o terceiro é: {resultado2}")
print(f"O terceiro elevado ao cubo é: {resultado3}")