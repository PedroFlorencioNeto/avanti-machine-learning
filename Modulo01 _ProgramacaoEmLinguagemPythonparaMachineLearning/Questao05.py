# ------------------------------------#
# Atlântico Avanti - Machine Learning # 
#                                     #
#  Pedro Florencio de Almeida Neto    #
#                                     #
#     pedroflorencio@alu.ufc.br       #
# ------------------------------------#

# 5. Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares

def extract_odd(list_numbers:list):
    '''Funcao que recebe uma lista de valores e retorna uma lista com os ímpares.

    Args: list_numbers (list) -> lista de numeros em análise.

    Returns: list_odds (list) -> lista de ímpares extraídos.
    
    '''
    list_odds = []
    
    for number in list_numbers:
        if number%2 != 0:
            list_odds.append(number)

    return list_odds

# Lista a ser recebida:
list_test = [2,5,6,34,3,2,1,6,0,8,6,21]

# Lista resposta:
list_resposta = extract_odd(list_test)

print(list_resposta)