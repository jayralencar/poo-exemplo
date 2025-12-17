class Pessoa:
    def __init__(self, nome, email, telefone):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
    
    @classmethod
    def from_dict(cls, data_dict):
        return cls(data_dict["nome"], data_dict["email"], data_dict['telefone'])
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
