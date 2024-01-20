# Herança

class Mae:

    def __init__(self, endereco) -> None:
        self.endereco = endereco
        self.sobrenome = 'Silva'

    def comer(self) -> None:
        print('Estou comendo')

    def estudar(self) -> None:
        print('Estou estudando')


class Filha(Mae):

    def __init__(self, endereco):
        super().__init__(endereco)

    def brincar(self, brinquedo: str) -> None:
        print('Estou brincando com {}' .format(brinquedo))

# Os métodos públicos são herdados pela filha


ana = Mae('Rua Elvira')
clara = Filha('Rua do Bolo')
clara.brincar('boneca')

print(ana.endereco)
print(clara.endereco)


class Neta(Filha):

    def __init__(self, endereco):
        super().__init__(endereco)
