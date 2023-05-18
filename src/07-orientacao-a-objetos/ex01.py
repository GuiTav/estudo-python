
from classes import Aluno



aluno1 = Aluno("sp1231232,João,joao@gmail.com")
aluno2 = Aluno("sp1231232,Não João,naojoao@gmail.com")
aluno3 = Aluno("sp3123123,Realmente não João,real_ofc_nao_joao@gmail.com")
# erro = Aluno(",tudo errado, erro@gmail.com")


print(aluno1 == aluno2)
print(aluno3 == aluno1)
