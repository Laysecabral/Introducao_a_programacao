from random import randint
Q = []
for numero in range(20):
    Q.append(randint(1, 100))

print(Q)

#variavel de controle
maior = -1
menor = 101

for item_da_lista in Q:
    if maior < item_da_lista:
        maior = item_da_lista

    if menor > item_da_lista:
        menor = item_da_lista

print(f'O maior valor é: {maior}')
print(f'O menor valor é: {menor}')

print(max(Q))
print(min(Q))