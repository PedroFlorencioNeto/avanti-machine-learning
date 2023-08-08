# ------------------------------------#
# Atlântico Avanti - Machine Learning # 
#                                     #
#  Pedro Florencio de Almeida Neto    #
#                                     #
#     pedroflorencio@alu.ufc.br       #
# ------------------------------------#

# 6. Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes.

def extract_prime(list_numbers:list):
    '''Funcao que recebe uma lista de valores e retorna uma lista com os primos.

    Args: list_numbers (list) -> lista de numeros em análise.

    Returns: list_prime (list) -> lista de primos extraídos.
    
    '''

    # Variáveis
    list_prime = []
    primo = False
    
    for number in list_numbers:
        if number in [1,2]:
            list_prime.append(number)
        else:
            for i in range(2,number):
                if number%i == 0:
                    break
                else:
                    list_prime.append(number)

    return list_prime

# Lista a ser recebida:
list_test = [2,5,6,34,3,2,1,6,0,8,6,21,13,60]

# Lista resposta:
list_resposta = extract_prime(list_test)

print(list_resposta)
