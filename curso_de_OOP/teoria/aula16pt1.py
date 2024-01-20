# Polimorfismo

""" É um princípio a partir do qual classes derivadas de uma
classe base são capazes de invocar os métodos que, embora
apresentem a mesma assinatura, comportam-se de maneira diferente
para cada uma das classes derivadas.
"""


class PessoaA:

    def se_apresentar(self):
        print('Olá, eu sou a pessoa A')


class PessoaB(PessoaA):

    def __init__(self):
        super().__init__()

    def se_apresentar(self):
        print('Estou alterando esse método')


class PessoaC(PessoaB):

    def __init__(self):
        super().__init__()


pessoa1 = PessoaA()
pessoa2 = PessoaB()
pessoa3 = PessoaC()

pessoa1.se_apresentar()
pessoa2.se_apresentar()
pessoa3.se_apresentar()

# A pessoa em PessoaC() herda de B e não A
