
from classes import Projeto



proj1 = Projeto("1,Laboratório de Desenvolvimento de Software,Pedro Gomes")
proj2 = Projeto("2,Laboratório de Visão Computacional,Domingos Latorre")
proj3 = Projeto("2,Repetido,Repetido")
proj4 = Projeto("3,Laboratório de Arduíno,Daniela")
# erro = Projeto(",Projeto inválido,sem responsável")


print(proj1 == proj2)
print(proj1 == proj3)
print(proj2 == proj3)
