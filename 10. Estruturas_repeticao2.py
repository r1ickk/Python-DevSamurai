# FOR percorre itens, muito usado em listas

for dia in ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']:
    print(dia)
    # Para cada dia em lista, mostre o dia

for numero in [0, 1, 2, 3, 4, 5]:
    print(numero)
# Para cada número em lista, mostre o número


for numero in [0, 1, 2, 3, 4, 5]:
    print(numero, end=" ")
# Para cada número em lista, mostre o número (Mas na horizontal)


# Range

for numero in range(6):
    print(numero, end="")
# Gerou uma sequência partindo do zero, 6 números.
#  Ela sempre vai gerar a partir do zero

for numero in range(5, 20):
    print(numero, end="")
    # Vai gerar uma sequência iniciando do 5 e indo até o 19

for numero in range(5, 20, 5):
    print(numero, end="")
    # Vai gerar uma sequência do 5 ao 20, indo de 5 em 5
