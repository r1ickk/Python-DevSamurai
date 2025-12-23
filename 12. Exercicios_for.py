# Faça um programa que gere uma tabela de multiplicação. O programa deverá perguntar ao usuário qual tabuada ele quer e até qual valor a tabuada será mostrada, sempre começando pelo zero.

tabuada = int(input("Qual tabuada será gerada? "))
limite = int(input("Até qual valor iremos calcular? "))
for numero in range(0, limite + 1):
    print(f'{tabuada} X {numero} = {tabuada*numero}')
    # f'{}' valor contido na tabuada, numero etc


# Faça um programa que calcule o enésimo elemento da série de Fibonacci. Lembrando que a série começa da seguinte forma: 1,1,2,3,5,8...

n = int(input("Digite o primeiro elemento: "))
primeiro = 1
segundo = 1

if n == 1 or n == 2:
    print('1')

else:
    for _ in range(2, n):  # _ o loop vai acontecer mas ele não será atribuído
        elemento = primeiro + segundo
        segundo = primeiro
        primeiro = elemento
    print(elemento)
