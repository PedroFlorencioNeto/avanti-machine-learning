# ------------------------------------#
# Atlântico Avanti - Machine Learning # 
#                                     #
#  Pedro Florencio de Almeida Neto    #
#                                     #
#     pedroflorencio@alu.ufc.br       #
# ------------------------------------#

# 4. Dada uma lista de strings ['banana','maçã','laranja','abacaxi'] crie uma nova
# lista com as palavras que têm mais de 5 letras e outra lista com as palavras que terminam
# com a letra a.

lista_frutas = ['banana','maçã','laranja','abacaxi']
lista_cinco = []
lista_a = []

for fruta in lista_frutas:
    if len(fruta) > 5:
        lista_cinco.append(fruta)
    
    if fruta[-1] in ['a','ã','â','á','à']:
        lista_a.append(fruta)

print(f'Lista das palavras com mais de 5 letras: {lista_cinco}\nLista das palavras que terminam com a: {lista_a}')

