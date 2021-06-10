alunos = int(input("Quantos alunos tem na turma: "))
materias = int(input("Quantas matérias eles estudam: "))

mediaTurma = 0
for aluno in range(alunos):
    print("Aluno", aluno + 1, ":")

    mediaAluno = 0
    for materia in range(materias):
        print("Nota da materia", materia + 1, ":", end='')
        nota = int(input())
        mediaAluno += nota

    mediaAluno /= materias
    print("Media desse aluno:", mediaAluno, "\n")

    mediaTurma += mediaAluno

mediaTurma /= alunos
print("Media da turma:", mediaTurma)