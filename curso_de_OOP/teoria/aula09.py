# Princípio Aberto/Fechado ('O' do SOLID)
# Open/Close Principle

""" Para que sistemas de software sejam mais fáceis de mudar,
eles devem ser projetados para permitir o comportamento desses
sistemas a serem alterados pela adição de novo código, em vez
de alterar códigos existentes.
"""


class Circo_:

    def apresentar(self, tipo):
        if tipo == 1:
            self.apresentar_malabarista()
        if tipo == 2:
            self.apresentar_palhaço()

    def apresentar_malabarista(self):
        print('Malabarista apresentando seu show')

    def apresentar_palhaço(self):
        print('Palhaço apresentando seu show')


# Um módulo é considerado aberto se ainda estiver disponível para extensão


class Circo:

    def apresentar_show(self, apresentador: any):
        apresentador.apresentar_show()


class Malabarista:

    def apresentar_show(self):
        print('Malabarista apresentando seu show')


class Palhaço:

    def apresentar_show(self):
        print('Palhaço apresentando seu show')


# A classe Circo está fechada para alterações mas aberta para extensões

circo = Circo()
malabarista = Malabarista()
palhaço = Palhaço()

circo.apresentar_show(malabarista)
circo.apresentar_show(palhaço)

# Se quisermos um novo objeto apresentando o show


class Domador:

    def apresentar_show(self):
        print('Domador apresentando seu show')


domador = Domador()
circo.apresentar_show(domador)
