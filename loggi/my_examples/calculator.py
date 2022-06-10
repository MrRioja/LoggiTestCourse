from time import sleep


class DivisionByZero(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


def soma(a: int, b: int):
    return a + b


def subtracao(a: int, b: int):
    return a - b


def divisao(a: int, b: int):
    if b < 1:
        raise DivisionByZero(message='Não é possivel dividir um numero por zero.')
    else:
        return a / b


def multiplicacao(a: int, b: int):
    return a * b


def raiz_quadrada(number: int):
    return number**(0.5)
