# 1. Calcule a soma dos dos numeros do 10 ao 14

somaTotal = sum([10, 11, 12, 13, 14])
print(somaTotal)

# 2. Calcule a média dos números 10, 15 e 20

mediaTotal = (10+15+20)/3
print(mediaTotal)

# 3. Peça ao usuário para digitar duas notas de zero a dez e os pesos das notas e calcule a média ponderada entre elas.
# Exemplo: media=(nota1*peso1+nota2*peso2)/(peso1+peso2)

nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
peso1 = float(input('Primeiro peso da nota: '))
peso2 = float(input('Segundo peso da nota: '))
media = (nota1*peso1+nota2*peso2)/(peso1+peso2)

print("A média entre {} e {} é igual a {}".format(nota1, nota2, media))


# 4. Qual o menor preço dessa lista?
# Preços: R$100,00. R$34,90. R$31,50. R$18,95.

print(min(100, 34.90, 31.50, 18.95))
