
class Projeto:
    def __init__(self, valores):
        codigo, titulo, responsavel = valores.split(",")

        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
        self.participacoes = []
    

    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, value):
        if str(value) != "":
            self._codigo = str(value)
        else:
            raise ValueError("O valor do código não pode ser vazio")
    

    @property
    def titulo(self):
        return self._titulo
    
    @titulo.setter
    def titulo(self, value):
        if str(value) != "":
            self._titulo = str(value)
        else:
            raise ValueError("O valor do título não pode ser vazio")
    

    @property
    def responsavel(self):
        return self._responsavel
    
    @responsavel.setter
    def responsavel(self, value):
        if str(value) != "":
            self._responsavel = str(value)
        else:
            raise ValueError("O valor do responsável não pode ser vazio")


    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.codigo == value.codigo
        return False
    

    def add_participacao(self, participacao):
        self.participacoes.append(participacao)




from ex01 import aluno1, aluno2, aluno3
from ex03 import Participacao

proj1 = Projeto("1,Laboratório de Desenvolvimento de Software,Pedro Gomes")
proj1.add_participacao(Participacao(1, "18/05/2023", "31/12/2023", aluno1, proj1))
proj1.add_participacao(Participacao(3, "18/05/2023", "31/12/2023", aluno2, proj1))

proj2 = Projeto("2,Laboratório de Visão Computacional,Domingos Latorre")
proj2.add_participacao(Participacao(2, "01/01/2023", "31/12/2023", aluno2, proj2))


for participacao in proj1.participacoes:
    print(participacao)


for participacao in proj2.participacoes:
    print(participacao)