class Calcolatrice:
    """Rappresenta una calcolatrice"""
    # metodo omettibile

    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def sott(self, x, y):
        return x - y

    def molt(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y

    def doppia_div(self, x, y):
        return x // y

    def mod(self, x, y):
        return x % y

    def pot(self, x, y):
        return x ** y
    # metodo omettibile

    def __del__(self):
        pass

# mettere tutto in una funzione
# eper poi inserirla in un loop
# sistemare con try except
#print(Calcolatrice().add(5, 4))


def calcolatrice():
    print('\nCALCOLATRICE\n')
    print('Inserisci un 1° numero, l\'operatore ed un 2° numero\n')
    try:
        a = int(input('inserisci il 1° numero: '))
        b = input('inserisci l\'operatore: ')
        c = int(input('inserisci il 2° numero: '))

        if b == '+':
            print(Calcolatrice().add(a, c))
        if b == '-':
            print(Calcolatrice().sott(a, c))
        if b == '*':
            print(Calcolatrice().molt(a, c))
        if b == '/':
            print(Calcolatrice().div(a, c))
        if b == '//':
            print(Calcolatrice().doppia_div(a, c))
        if b == '%':
            print(Calcolatrice().mod(a, c))
        if b == '**':
            print(Calcolatrice().pot(a, c))
    except:
        print('formato non valido, inserisci un numero')
        calcolatrice()


if __name__ == '__main__':
    calcolatrice()
