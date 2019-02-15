def quantidadedecabos():
    qtd = input('Quantidades: ')

    try:
        return int(qtd)
    except Exception as err:
        print('Digite Somente Numeros Inteiros! ')
    return quantidadedecabos()

print(quantidadedecabos())

