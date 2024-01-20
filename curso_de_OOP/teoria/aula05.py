# Princípio da Únida Responsabilidade
# Single Responsability Principle (S do SOLID)

# SRP:
""" Um módulo deve ser responsável por um, e apenas um, ator"""

# Módulo = um conjunto coeso de funções e estruturas de dados


class SistemaCadastral_:

    def cadastrar(self, nome: str, idade: int) -> None:
        if isinstance(nome, str) and isinstance(idade, int):
            print('acessando o banco de dados...')
            print('Cadastrar o Usuário {}, Idade {}' .format(nome, idade))
        else:
            print('dados inválidos!')

# Isso é problemático segundo o princípio da responsábilidade única
# É mais interessante separar a partir de um certo contexto
# Como abaixo:


class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__verificar_dados(nome, idade):
            self.__armazenar_usuario(nome, idade)
        else:
            self.__indicar_erro()

    def __verificar_dados(self, nome: str, idade: int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        else:
            return False

    def __armazenar_usuario(self, nome: str, idade: int) -> None:
        print('acessando o banco de dados...')
        print('Cadastrar o Usuário {}, Idade {}' .format(nome, idade))

    def __indicar_erro(self):
        print('dados inválidos!')

# Teste


sis = SistemaCadastral()
sis.cadastrar('Lhama', 43)
