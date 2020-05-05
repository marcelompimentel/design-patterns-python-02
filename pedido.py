# -*- coding: UTF-8 -*-

from datetime import date
from abc import ABCMeta, abstractmethod

class Pedido(object):
    def __init__(self, cliente, valor):
        self.__cliente = cliente
        self.__valor = valor
        self.__status = 'NOVO'
        self.__data_finalizacao = None

    def paga(self):
        self.__status = 'PAGO'

    def finaliza(self):
        self.__data_finalizacao = date.today()
        self.__status = 'ENTREGUE'

    @property
    def cliente(self):
        return self.__cliente

    @property
    def valor(self):
        return self.__valor

    @property
    def status(self):
        return self.__status

    @property
    def data_finalizacao(self):
        return self.__data_finalizacao


class Fila_de_trabalho(object):
    def __init__(self):
        self.__comandos = []

    def adiciona(self, comando):
        self.__comandos.append(comando)

    def processa(self):
        for comando in self.__comandos:
            comando.executa()


class Comando(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def executa(self):
        pass


class Paga_pedido(Comando):
    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.paga()


class Conclui_pedido(Comando):
    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.finaliza()


if __name__ == '__main__':
    pedido1 = Pedido('Simba', 550)
    pedido2 = Pedido('Nina', 350)
    pedido3 = Pedido('Raj', 600)

    comando1 = Paga_pedido(pedido1)
    comando2 = Conclui_pedido(pedido1)
    comando3 = Paga_pedido(pedido2)
    comando4 = Paga_pedido(pedido3)
    comando5 = Conclui_pedido(pedido3)

    fila = Fila_de_trabalho()

    fila.adiciona(comando1)
    fila.adiciona(comando2)
    fila.adiciona(comando3)
    fila.adiciona(comando4)
    fila.adiciona(comando5)
    fila.processa()
 
    print('Status Pedido 1: {}'.format(pedido1.status))
    print('Status Pedido 2: {}'.format(pedido2.status))
    print('Status Pedido 3: {}'.format(pedido3.status))