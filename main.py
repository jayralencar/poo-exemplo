from src.estudante import Estudante

p = Estudante.from_dict({
    "nome": "Jayr",
    "email": "jayr.pereira@ufca.edu.br",
    "telefone": "889881232"
})

print("Meu nome é ", p.nome)