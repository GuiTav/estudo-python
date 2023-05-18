
class Projeto:
    def __init__(self, valores):
        codigo, titulo, responsavel = valores.split(",")

        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
    

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



proj1 = Projeto("1,Laboratório de Desenvolvimento de Software,Pedro Gomes")
proj2 = Projeto("2,Laboratório de Visão Computacional,Domingos Latorre")
proj3 = Projeto("2,Repetido,Repetido")
proj4 = Projeto("3,Laboratório de Arduíno,Daniela")
# erro = Projeto(",Projeto inválido,sem responsável")


print(proj1 == proj2)
print(proj1 == proj3)
print(proj2 == proj3)
