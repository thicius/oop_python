from typing import Type


class Conexao:

    def conectar(self):
        print('Conectando ao banco de dados')

    def desconectar(self):
        print('Desconectando ao banco de dados')


class MysqlRepo(Conexao):

    def __init__(self):
        super().__init__()

    def select(self):
        self.conectar()
        print('SELECT * FROM table')


class CasoDeUso:

    def buscar(self, db_repo: Type[MysqlRepo]):
        db_repo.select()


# Testes

mysql = MysqlRepo()
caso = CasoDeUso()
caso.buscar(mysql)
