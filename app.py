
def quantidade_frutas():
    # converter para inteiros antes de comparar
    quantidade_macas = int(input('Qual a quantidade de maçãs? '))
    quantidade_bananas = int(input('Qual a quantidade de bananas? '))

    if quantidade_macas < quantidade_bananas:
        print('A quantidade de bananas é maior que a quantidade de maçãs')
    elif quantidade_macas > quantidade_bananas:
        print('A quantidade de maçãs é maior que a quantidade de bananas')
    else:
        print('As quantidades de maçãs e bananas são iguais')


if __name__ == '__main__':
    quantidade_frutas()
