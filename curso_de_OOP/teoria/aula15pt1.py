# Princípio da Substituição de Liskov
# LSP: Liskov Substitution Principle

""" Para construir sistemas de software a partir de partes intercambiáveis,
essas ártes devem aderir a um contrato que permitem que essas partes sejam
substituídas umas pelas outras.
"""


class PessoaA:

    def se_apresentar(self):
        print('Ola, sou a pessoa A')


class PessoaB:

    def __init__(self):
        super().__init__()

    def se_apresentar(self):
        print('Estou alterando esse método')


pessoa = PessoaA()
pessoa.se_apresentar()

pessoa2 = PessoaB()
pessoa2.se_apresentar()

# Para um mesmo método o comportamento foi diferente para a herança
# Isso é uma quebra do princípio de Liskov

""" Isso é uma quebra do princípio de Liskov, já que o método de Liskov afirma
que o método deve ter a mesma funcionalidade tanto para a classe inicial quanto
 para a que herda.
"""
