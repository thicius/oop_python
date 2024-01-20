# Associação de Classes

# Veremos associação (Pessoa -> Interruptor)

from typing import Type


class Interruptor:

    def __init__(self, comodo):
        self.__comodo = comodo

    def acender(self):
        print('acendendo {}' .format(self.__comodo))

    def apagar(self):
        print('apagando {}' .format(self.__comodo))


class Pessoa:

    def acender_luz(self, interruptor: type(Interruptor)):   # A tipagem do Interrputor é
        interruptor.acender()

    def apagar_luz(self, interruptor: type(Interruptor)):
        interruptor.apagar()

    def dormir(self):
        print('Fui dormir')


thiago = Pessoa()
interruptor_quarto = Interruptor('quarto')

interruptor_quarto.acender()

interruptor_cozinha = Interruptor('cozinha')
thiago.apagar_luz(interruptor_cozinha)
thiago.dormir()

# A pessoa consegue interagir com um objeto interruptor
