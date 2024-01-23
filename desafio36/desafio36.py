#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

valor_casa = float(input('Digite o valor da casa. R$'))
salário = float(input('Digite o seu salário R$'))
anos = int(input('Digite em quantos anos irá pagar: '))

meses = anos * 12
prestacoes = valor_casa // meses
print(prestacoes) 