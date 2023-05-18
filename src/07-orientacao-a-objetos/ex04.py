
import classes


aluno1 = classes.Aluno("sp98765432,André Luiz,andluiz@gmail.com")
aluno2 = classes.Aluno("sp11901002,Paulo Roberto,paulorob@gmail.com")

proj1 = classes.Projeto("1,Laboratório de Desenvolvimento de Software,Pedro Gomes")
proj1.add_participacao(classes.Participacao(1, "18/05/2023", "31/12/2023", aluno1, proj1))
proj1.add_participacao(classes.Participacao(3, "18/05/2023", "31/12/2023", aluno2, proj1))

proj2 = classes.Projeto("2,Laboratório de Visão Computacional,Domingos Latorre")
proj2.add_participacao(classes.Participacao(2, "01/01/2023", "31/12/2023", aluno2, proj2))


for participacao in proj1.participacoes:
    print(participacao)


for participacao in proj2.participacoes:
    print(participacao)