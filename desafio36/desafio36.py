# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

valor_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o seu salário: R$'))
anos = int(input('Digite em quantos anos irá pagar: '))

prestacao = valor_casa / (anos * 12)
if prestacao > salario * 30 / 100:
    print(f'Empréstimo recusado, o valor de prestação para pagar uma casa de R${"{:.2f}".format(valor_casa)} é de R${"{:.2f}".format(prestacao)} é maior que 30% do seu salário que é R${"{:.2f}".format(salario)}')
else:
    print(f'Empréstimo aceito, o valor de prestação para pagar uma casa de R${"{:.2f}".format(valor_casa)} é de R${"{:.2f}".format(prestacao)} é menor que 30% do seu salário que é R${"{:.2f}".format(salario)}')
