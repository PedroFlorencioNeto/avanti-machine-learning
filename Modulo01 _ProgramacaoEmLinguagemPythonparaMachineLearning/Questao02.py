# ------------------------------------#
# Atlântico Avanti - Machine Learning # 
#                                     #
#  Pedro Florencio de Almeida Neto    #
#                                     #
#     pedroflorencio@alu.ufc.br       #
# ------------------------------------#

# 2. Escreva um programa que leia números digitados pelo usuário e pare quando o número 0 for digitado.
#    No final, imprima a média dos números digitados

num_digitados = []
num = float(input('Digite um numero: '))

while num !=0:
    num_digitados.append(num)
    num = float(input('Digite um numero: '))
    avg = sum(num_digitados)/len(num_digitados)

print(f'A média dos algarismos digitados é {avg}')
