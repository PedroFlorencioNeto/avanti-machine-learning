# ------------------------------------#
# Atlântico Avanti - Machine Learning # 
#                                     #
#  Pedro Florencio de Almeida Neto    #
#                                     #
#     pedroflorencio@alu.ufc.br       #
# ------------------------------------#

# 9. Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa,
# e retorne a lista ordenada pelo nome das pessoas em ordem alfabética

def retorna_nomes(pessoas:list):
    list_names = []

    for pessoa in pessoas:
        # povoando lista apenas com os nomes
        list_names.append(pessoa[0])

        # ordenando em ordem alfabética
        list_names.sort()

    return list_names

# Lista exemplo
list_pessoas=[('Romulo',35),('Anderson',37),('Gabrielle',38),('Pedro',26)]

print(retorna_nomes(list_pessoas))