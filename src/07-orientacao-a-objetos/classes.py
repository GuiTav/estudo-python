

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




class Projeto:
    def __init__(self, valores):
        codigo, titulo, responsavel = valores.split(",")

        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
        self.participacoes= []
    

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




class Participacao():
    def __init__(self, codigo, data_inicio, data_fim, aluno, projeto):
        self.codigo = codigo
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.aluno = aluno
        self.projeto = projeto


    def __str__(self):
        return f"Participacao[codigo={self.codigo}, data_inicio={self.data_inicio}, data_fim={self.data_fim}, aluno={self.aluno}, projeto={self.projeto}]"