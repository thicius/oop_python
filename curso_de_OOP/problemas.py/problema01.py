# Criando a Classe:

class Elevador:
    def __init__(self, numero: int) -> None:
        self.numero = numero

    def locomover(self, novo_andar: int) -> None:
        if novo_andar < 1 or novo_andar > 15:
            return self.__mensagem_de_erro()
        else:
            self.andar = novo_andar
            return self.__locomoveu_com_sucesso()

    def __locomoveu_com_sucesso(self) -> None:
        return print('O elevador {} foi para o andar {}' .format(self.numero, self.andar))

    def __mensagem_de_erro(self) -> None:
        return print('Esse andar não existe')


elevador1 = Elevador(1)
elevador2 = Elevador(2)

# Arrumando o input

numero_do_elevador, novo_andar = map(int, input().split())

if numero_do_elevador == 1:
    elevador1.locomover(novo_andar)
elif numero_do_elevador == 2:
    elevador2.locomover(novo_andar)
else:
    print('Só temos dois elevadores')
