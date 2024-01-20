# Encapsulamento em Heranças

""" Elementos protected são acessíveis apenas pela
própria classe mas também pela sua herança.

self.user = público
self._user = protegido
self.__user = privado
"""


class DatabaseConn:

    def __init__(self) -> None:
        self.__database = 'Postgres'
        self._conn = '//connection_string'
        self.user = 'Thiago'

    def get_database(self) -> None:
        print(self.__database)

    def _testing_conection(self) -> None:
        print('Connection Ok!')


class Repository(DatabaseConn):

    def __init__(self) -> None:
        super().__init__()
        print(self.user)
        # print(self.__database) Error
        print(self._conn)

    def select(self) -> None:
        self._testing_conection()
        print('connecting to {}' .format(self._conn))
        print('SELECT * FROM table')


repo = Repository()
repo.select()
