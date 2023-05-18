
class Aluno:
    def __init__(self, valores):
        prontuario, nome, email = valores.split(",")

        self.prontuario = prontuario
        self.nome = nome
        self.email = email
    

    @property
    def prontuario(self):
        return self._prontuario
    
    @prontuario.setter
    def prontuario(self, value):
        if str(value) != "":
            self._prontuario = str(value)
        else:
            raise ValueError("O valor do prontuário não pode ser vazio")
    

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, value):
        if str(value) != "":
            self._nome = str(value)
        else:
            raise ValueError("O valor do nome não pode ser vazio")
    

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if str(value) != "":
            self._email = str(value)
        else:
            raise ValueError("O valor do email não pode ser vazio")


    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.prontuario == value.prontuario
        return False



aluno1 = Aluno("sp1231232,João,joao@gmail.com")
aluno2 = Aluno("sp1231232,Não João,naojoao@gmail.com")
aluno3 = Aluno("sp3123123,Realmente não João,real_ofc_nao_joao@gmail.com")
# erro = Aluno(",tudo errado, erro@gmail.com")


print(aluno1 == aluno2)
print(aluno3 == aluno1)
