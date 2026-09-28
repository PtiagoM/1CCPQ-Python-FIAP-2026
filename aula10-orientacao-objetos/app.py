from aluno import Aluno
from disciplina import Disciplina

# criar / instalar i aluno
aluno1 = Aluno("Russi", 12345678, "Ciência da Computação")

# criar 2 disciplinas
cs = Disciplina("Computer Science", "Lucas")
model_mat = Disciplina("Modelagem Matemática", "Christiam")

#matricular o aluno na disciplina
aluno1.matricular(cs)
aluno1.matricular(model_mat)

#adicionar notas do aluno,
aluno1.adicionar_nota(cs, 10)
aluno1.adicionar_nota(cs, 10)
aluno1.adicionar_nota(cs, 10)
aluno1.adicionar_nota(model_mat, 9)
aluno1.adicionar_nota(model_mat, 10)
aluno1.adicionar_nota(model_mat, 10)

print(aluno1.exibir_boletim)