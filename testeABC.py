# Testando como fazer quando for necessário impor algum metódo para uma classe, através das classes ABC

from collections.abc import MutableSequence

class MinhaListinhaMutavel(MutableSequence):
    pass


objetoValidado = MinhaListinhaMutavel()
print(objetoValidado)
# vai da erro dizendo todos os métodos que precisamos implementar para herdar o comportamento da MutableSequence, por ex