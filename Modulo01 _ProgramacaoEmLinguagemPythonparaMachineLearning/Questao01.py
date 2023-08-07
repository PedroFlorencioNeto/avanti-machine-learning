# ------------------------------------#
# Atlântico Avanti - Machine Learning # 
#                                     #
#  Pedro Florencio de Almeida Neto    #
#                                     #
#     pedroflorencio@alu.ufc.br       #
# ------------------------------------#

# 1. Escreva um programa que solicite ao usuário uma palavra e verifique se ela é palíndromo

palavra = input('Entre com a palavra: ')

if palavra.upper() == palavra[::-1].upper():
    print('É um palídromo')

else: print('Não é um palíndromo')

# Observações: O uso do método upper() é para garantir que o uso de letras maiúsculas e minúsculas
#              não influenciem na comparação das palavras.