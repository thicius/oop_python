from typing import Dict, Type


class Repositorio:

    def select(self, nome: str) -> Dict:
        return {"nome": nome, "idade": 32}

    def insert(self, nome: str, idade: int) -> Dict:
        print('Inserindo Dados {}, {}' .format(nome, idade))
        return {"nome": nome, "idade": idade}


class Insersor:

    def __init__(self, repositorio: Type[Repositorio]) -> None:
        self.__repo = repositorio

    def inserir_dado(self, nome: str, idade: int) -> Dict:
        registro = self.__repo.select(nome)
        if registro:
            raise Exception('O regisito já existe!')

        novo_registro = self.__repo.insert(nome, idade)
        return novo_registro


class RepositorioFaker(Repositorio):
    def __init__(self):
        super().__init__()

    def select(self, name: int) -> None:
        return None

# Run


repo = RepositorioFaker()
insersor = Insersor(repo)
data = insersor.inserir_dado('Thiago', 18)
print(data)
