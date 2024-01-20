class MinhaClasse:

    estatico = 'lhama'          # Não é recomendado
    # Já que pode ser abstraido com self.estatico dentro do __init__

    def __init__(self, estado):
        self.estado = estado

    def print_estatico(self):
        estatico = 3
        print(estatico)

    def print_estatico2(self):
        print(self.estatico)

    @classmethod
    def mudar_estatico(cls):   # Estamos falando da classe em si
        cls.estatico = 'Programador'


obj1 = MinhaClasse(True)
obj2 = MinhaClasse(False)

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)     # É como um contexto geral
# Os três rodam

obj1.estatico = 'Programador'
print(obj1.estatico)
# Foi possível alterar

# Se alterar desse modo:
MinhaClasse.estatico = 'Programador'
# todos os três acima mudam

# O contexto da classe é passado pros objetos
# Mas o contexto dos objetos ficam somente armazenados neles
MinhaClasse.estatico = 'Programador'
obj2.estatico = 'Lhama'
print(obj1.estatico, obj2.estatico)

obj2.print_estatico()
obj2.print_estatico2()

# Olhando para o mudar_estatico()

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(False)

obj1.mudar_estatico()

obj1.print_estatico2()
obj2.print_estatico2()

# Vai mudar tanto pro obj1, quanto pro obj2
