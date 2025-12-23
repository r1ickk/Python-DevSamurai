#  Faça um programa que calcule o fatorial de um número fornecido pelo usuário. Exemplo, 5 fatorial: 5! = 5*4*3*2*1

numero = int(input('Digite um número inteiro: '))
fatorial = numero
while numero >= 2:
    fatorial = fatorial * (numero - 1)
    numero -= 1  # numero = numero - 1

print(fatorial)


# Vamos fazer um programa que simule um cofre. Ele terá uma senha predefinida e o usuário terá três tentativas para acertar a senha. A cada tentativa errada, o programa deverá mostrar a mensagem: Senha incorreta. Tente novamente. Se ele acertar a senha, o programa deverá mostrar a mensagem: Senha correta, acesso concedido

senha = "0000"
tentativas = 3

while tentativas != 0:
    tentativa = input("Digite uma senha numérica de 4 digitos: ")

    if tentativa == senha:
        print("Senha correta! Acesso concedido.")
        break  # Para o loop

    else:
        print("Senha incorreta! Tente novamente")
        tentativas -= 1
