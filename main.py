from src.pessoa import Pessoa

p = Pessoa.from_dict({
    "nome": "Jayr",
    "email": "jayr.pereira@ufca.edu.br",
    "telefone": "889881232"
})

print(p.nome)