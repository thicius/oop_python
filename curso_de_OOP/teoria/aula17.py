# Métodos e Classes Abstratas


from abc import ABC, abstractmethod


class AbstractClass(ABC):

    def __init__(self):
        self.atributo = 'Olá Mundo'

    def metodo(self, elemento: str) -> None:
        print(elemento)

    @abstractmethod
    def metodo_abstrato(self) -> None:
        pass


class Filha(AbstractClass):

    def apresentar_metodo(self) -> None:
        print(self.atributo)

    def metodo_abstrato(self) -> None:
        print('Implementando metodo abstrato')


filha = Filha()
filha.apresentar_metodo()
filha.metodo('Estou aqui')

abstractClass = AbstractClass()
abstractClass.metodo('Fazendo algo')

# No Python, para ter uma classe abstrata é necessário ter no mínimo um método abstrato

""" Não podemos fazer instâncias de classes abstratas.
"""
