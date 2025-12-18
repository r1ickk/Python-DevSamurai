# 1. Faça um programa que recebe do usuário duas notas de zero a dez, e escreva na tela "Você estpa aprovado, PARABÉNS!!!" se a medida das duas notas for maior que sete.
# 2. Faça um programa que recebe do usuário duas notas de zero a dez, e escreva na tela "Você estpa aprovado, PARABÉNS!!!" se a medida das duas notas for maior que sete, e "Você não esrá aprovado" se a media for menor que sete.
# 3. Ainda usando o exemplo da média, acrescente uma terceira condição se, a media for maior ou igual a cindo e menor que sete, escreva na tela "Você está de recuperação".

# 1
nota1 = eval(input('Informe a primeira nota: '))
nota2 = eval(input('Informe a segunda nota: '))

if (nota1 + nota2) / 2 > 7:
    print("Você está aprovado, PARABÉNS!!!")
else:
    exit

# 2
nota1 = eval(input('Informe a primeira nota: '))
nota2 = eval(input('Informe a segunda nota: '))

if (nota1 + nota2) / 2 >= 7:
    print("Você está aprovado, PARABÉNS!!!")
else:
    print("Você não está aprovado")

# 3
nota1 = eval(input('Informe a primeira nota: '))
nota2 = eval(input('Informe a segunda nota: '))

if (nota1 + nota2) / 2 > 7:
    print("Você está aprovado, PARABÉNS!!!")
elif (nota1 + nota2) / 2 >= 5 < 7:
    print("Você está de recuperação")
else:
    print("Você não está aprovado")
