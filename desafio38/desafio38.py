#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#O primeiro valor é maior. O segundo valor é maior. Não existe valor amior, os dois são iguais

valor1 = int(input('Primeiro valor: '))
valor2= int(input('Segundo valor: '))

if valor1 == valor2:
    print("Não existe valor maior, os dois são iguais")
elif valor1 > valor2:
    print(f"O valor {valor1} é maior que o valor {valor2}")
elif valor2 > valor1:
    print(f"O valor {valor2} é maior que o valor {valor1}")