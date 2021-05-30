class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas.')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')  # if mes = True, fica mes = none

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

class Hipster:
    def __str__(self):
        return f'Hipster,  {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura, Caelum, Hipster):
    pass


jose = Junior('José')
jose.busca_perguntas_sem_resposta()
# como a classe Junior não tem a função busca_perguntas_sem_resposta, puxou a info da classe mãe
print("-----------------------------------")

# com a classe Pleno, a mesma coisa. Primeiro vai procurar em Alura, depois em Caelum e depois em Hipster
luan = Pleno('Luan')
luan.busca_perguntas_sem_resposta()  # puxou de Alura
luan.busca_cursos_do_mes()  # Alura não tinha essa função, então puxou de Caelum
luan.mostrar_tarefas()  # voltou a puxar de Alura
print(luan)  # agora não tem como printar nem Alura, nem Caelum, então fomos para Hispter que tem o __str__