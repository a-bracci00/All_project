def contarighe(nomefile):
    conta = 0
    for riga in open(nomefile):
        conta += 1
    return conta


if __name__ == '__main__':
    print(contarighe('wc.py'))
