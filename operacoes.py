# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod

class Expressao(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def avalia(self):
        pass


class Soma(Expressao):
    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self):
        return self.__expressao_esquerda.avalia() + self.__expressao_direita.avalia()


class Subtracao(Expressao):
    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self):
        return self.__expressao_esquerda.avalia() - self.__expressao_direita.avalia()


class Numero(Expressao):
    def __init__(self, numero):
        self.__numero = numero

    def avalia(self):
        return self.__numero


if __name__ == '__main__':
    expressao_esquerda = Soma(Numero(25), Numero(35))
    expressao_direita = Subtracao(Numero(10), Numero(5))
    expressao_conta = Soma(expressao_esquerda, expressao_direita)
    print(expressao_conta.avalia())