# Encapsulamento
# permissões de uso/ contexto

class Pessoa:

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def print_cpf(self):
        print(self.__cpf)

    def correr(self):
        print('Estou correndo')

    def __apresentar_documento(self):
        print(self.__cpf)

    def beber(self, bebida):
        if bebida == 'cerveja':
            self.__apresentar_documento()
        print('bebendo')


ronaldo = Pessoa('Ronaldo', 32, '03232ad23')
print(ronaldo.nome)
print(ronaldo.idade)
ronaldo.print_cpf()

# print(ronaldo.__cpf) não prestaria

ronaldo.beber('cerveja')
ronaldo.beber('coca-cola')
