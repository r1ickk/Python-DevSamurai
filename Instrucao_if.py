# Famoso SE. Se uma condição for verdadeira, ele executará o código.
temp = eval(input('Digite a temperatura: '))

if temp >= 30:
    print('Está muito calor!!!')
elif temp > 20:
    print('Está agradável!!!')
else:
    print('Está frio!!!')
