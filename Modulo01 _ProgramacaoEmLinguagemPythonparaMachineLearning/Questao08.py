# ------------------------------------#
# Atlântico Avanti - Machine Learning # 
#                                     #
#  Pedro Florencio de Almeida Neto    #
#                                     #
#     pedroflorencio@alu.ufc.br       #
# ------------------------------------#

# 8. Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor da lista.
def second_value(lista_num:list):

    lista_num.sort(reverse=True)

    return lista_num[1]

lista_teste = [2,5,4,67,1,0]

segundo_num = second_value(lista_teste)

print(segundo_num)