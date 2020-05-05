# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from impressora import Impressora

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

    @property
    def expressao_esquerda(self):
        return self.__expressao_esquerda

    @property
    def expressao_direita(self):
        return self.__expressao_direita

    def aceita(self, visitor):
        visitor.visita_soma(self)


class Subtracao(Expressao):
    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self):
        return self.__expressao_esquerda.avalia() - self.__expressao_direita.avalia()

    @property
    def expressao_esquerda(self):
        return self.__expressao_esquerda

    @property
    def expressao_direita(self):
        return self.__expressao_direita

    def aceita(self, visitor):
        visitor.visita_subtracao(self)


class Numero(Expressao):
    def __init__(self, numero):
        self.__numero = numero

    def avalia(self):
        return self.__numero

    def aceita(self, visitor):
        visitor.visita_numero(self)


if __name__ == '__main__':
    expressao_esquerda = Soma(Numero(25), Numero(35))
    expressao_direita = Subtracao(Numero(10), Numero(5))
    expressao_conta = Soma(expressao_esquerda, expressao_direita)

    impressora = Impressora()
    expressao_conta.aceita(impressora)