# Métodos Estáticos

# Contexto que não se associa ao contexto geral da Classe nem ao do Objeto
# É chamado contexto aplicado

class MinhaClasse:

    def __init__(eslf, estado):
        self.estado = estado

        @staticmethod
        def metodo_estatico():
            # print(self.estado) não funcionário porque "self" não é definido, nem "cls"
            print('Estou no meu método estático :D')


obj = MinhaClasse(True)

# Ambos abaixo funcionam

obj.metodo_estatico()
MinhaClasse.metodo_estatico()


class Error:

    @staticmethod
    def protocolo():
        print('Protocolo apresenta erro')

    @staticmethod
    def entrada():
        print('Parâmetros incorretos')

    @staticmethod
    def error_500():
        print('Internal Server Error')

    def error_400():
        print('Not Found')


Error.entrada()

# Podemos usar os staticmethod como se fossem coleções de contextos
# Que não estão diretamente ligados entre si
# E que não precisa de um objeto nessa classe.
