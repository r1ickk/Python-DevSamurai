# 1. Avalie se o número digitado pelo usuário é par ou ímpar. Se for par, a saída deve mostrar True, se ímpar, deverá mostrar False.

num1 = int(input('Informe o número desejado: '))
if num1 % 2 == 0:
    # O símbolo de porcento retorna o resto da divisão
    print(True)
else:
    print(False)


# # 2. Verifique se o menor preço dessa lista é menor que R$20,00
# # preços: R$100.20, R$34.90, R$31.50 e R$18.95

menor_preco = min(100.20, 34.90, 31.50, 18.95)
print(menor_preco)

if menor_preco >= 20.00:
    print(True)
else:
    print(False)

    # Ou então, poderíamos fazer da seguinte maneira:
    menor_preco = min(100.20, 34.90, 31.50, 18.95) < 20
print(menor_preco)

# # 3. Faça um programa que conevrta a temperatura em graus Fahrenheit fornecia pelo usuário em graus Celsius.
# # celsius = (5/9)*(fahrenheit - 32)

fahrenheit = float(input('Informe a temperatura em Fahrenheit: '))

celsius = (5/9) * (fahrenheit - 32)
print(f'{celsius} °C')
