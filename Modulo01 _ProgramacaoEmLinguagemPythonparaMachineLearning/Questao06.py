# ------------------------------------#
# Atlântico Avanti - Machine Learning # 
#                                     #
#  Pedro Florencio de Almeida Neto    #
#                                     #
#     pedroflorencio@alu.ufc.br       #
# ------------------------------------#

# 6. Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes.

def verifica_primo(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def primo_lista(numbers):
    primo_nums = []
    for num in numbers:
        if verifica_primo(num):
            primo_nums.append(num)
    return primo_nums

# Lista a ser recebida:
list_test = [2,5,6,34,3,2,1,6,0,8,6,21,13,60]

lista_primos = primo_lista(list_test)

print(lista_primos)

# Observação: Apenas para esta questão fiz o uso do ChatGPT devido ao tempo gasto
# com diversos erros na construção da minha própria função.
