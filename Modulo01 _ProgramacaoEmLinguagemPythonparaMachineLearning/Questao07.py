# ------------------------------------#
# Atlântico Avanti - Machine Learning # 
#                                     #
#  Pedro Florencio de Almeida Neto    #
#                                     #
#     pedroflorencio@alu.ufc.br       #
# ------------------------------------#

# 7. Escreva uma função que receba duas listas e retorne outra lista com os elementos
#    que estão presentes em apenas uma das listas

unique_list = []

def unique_elements(lista_a:list, lista_b:list):
    for numero in lista_a:
        if numero not in lista_b:
            unique_list.append(numero)

    for numero in lista_b:
        if numero not in lista_a:
            unique_list.append(numero)
            
    return unique_list

# Lista a ser recebida:
list_a = [2,5,6,34,3,2,1,6,0,8,6,21,13]
list_b= [67,2,6,34,3,87,1,6,6,8,6,21,14]

# Lista resposta:
list_resposta = unique_elements(list_a, list_b)

print(list_resposta)
