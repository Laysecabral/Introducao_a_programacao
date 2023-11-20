#with open('carro.txt, 'w', encoding=utf-8) as file:
#    file.write('corsa\n')
#    file.write('gurgel\n')
#    file.write('fusca\n')

with open('carro.txt', 'a', encoding='utf-8') as arquivo:

    for i in range(3):
        meu_carro = input('Digite um novo carro:')
        arquivo.write(meu_carro + '\n')
