# Encapsulamento e métodos Getter e Setters

class Pessoa:

    def __init__(self, name: str, idade: int) -> None:
        self.name = name
        self.idade = idade

    def dirigir(self, veiculo: str) -> None:
        print('Dirigindo um(a) {}' .format(veiculo))

    def cantar(self) -> None:
        print('Lalalala')

    def apresentar_idade(self) -> int:      # Retorna um inteiro
        return self.idade


class Alarme:

    def __init__(self, estado: bool) -> None:
        self.__estado = estado                  # colocar o __antes chama "encapsular"

    def get_estado(self) -> bool:
        return self.__estado

    def set_estado(self, valor: bool) -> None:
        self.__estado = valor
