# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1- para bara binário 2- para octal 3- para hexadecimal

numero = int(input('Digite um número inteiro: '))
print("""Escolha uma dentre as opções:
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal""")

escolha = int(input('Escolha um dos números: '))

if escolha > 3:
    print('Não existe esta opção')
elif escolha == 1:
    print(f"O número {numero} convertido em Binário ficou {format(numero, 'b')}")
elif escolha == 2:
    print(f"O número {numero} convertido em Octal ficou {format(numero, 'o')}")
elif escolha == 3:
    print(f"O número {numero} convertido em Hexadecimal ficou {format(numero, 'x')}")